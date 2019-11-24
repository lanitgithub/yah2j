from har_models import har_data_from_dict, Entry
from typing import Set, List, Tuple, Dict
from datetime import datetime
import json
import logging
import copy

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] %(levelname)-12s|process:%(process)-5s|thread:%(thread)-5s|funcName:%(funcName)s|message:%(message)s",
    handlers=[
        # logging.FileHandler('fileName.log'),
        logging.StreamHandler()
    ])

STATIC_TYPES = ['javascript', 'woff', 'css', 'image', 'video', 'audio']
MILLISEC_IN_MUNUTE = 60000


def get_mime_types(entries: List[Entry]) -> Set[str]:
    all_mime_types = []
    for entry in entries:
        all_mime_types.append(entry.response.content.mime_type)
    logging.debug(f'all_mime_types {type(all_mime_types)} = {all_mime_types}')
    return set(all_mime_types)


def get_type_lists(mime_types: List[str]) -> List[str]:
    static_types = []
    for mime_type in mime_types:
        is_static = False
        for stype in STATIC_TYPES:
            if stype in mime_type:
                is_static = True
                break
        logging.debug(f'mime_type {type(mime_type)} = {mime_type}')
        logging.debug(f'is_static {type(is_static)} = {is_static}')
        if is_static:
            static_types.append(mime_type)
    return static_types


def grouping_by_comment(entries: List[Entry], static_mime_types: List[str]):
    comments = {}
    group_number = 1
    for entry in entries:
        current_comment = entry.comment
        if current_comment == '':
            current_comment = 'non-comment'
        if current_comment not in comments:
            comments[current_comment] = group_number
            group_number += 1
    logging.debug(f'comments {type(comments)} = {comments}')

    grouped_entries = {}
    grouped_entries['entries'] = {}
    grouped_entries['comments'] = comments

    for comment in comments:
        grouped_entries['entries'][comment] = {'static': [], 'non-static': []}
        grouped_entries['entries'][comment]['group_number'] = comments[comment]

    for entry in entries:
        current_comment = entry.comment
        if current_comment == '':
            current_comment = 'non-comment'
        if entry.response.content.mime_type in static_mime_types:
            grouped_entries['entries'][current_comment]['static'].append(entry)
        else:
            grouped_entries['entries'][current_comment]['non-static'].append(
                entry)
    return grouped_entries


def set_types(entries, mime_types, static_mime_types):
    entries['mime_types'] = mime_types
    entries['static_mime_types'] = static_mime_types
    return entries


def set_times_in_entries(entries_data):
    for entry_group_name in entries_data['entries']:
        group_start_epoch = 0
        group_end_epoch = 0

        group_static_time_millisec = 0
        for entry in entries_data['entries'][entry_group_name]['static']:
            current_entry: Entry = entry
            if group_start_epoch == 0:
                group_start_epoch = current_entry.started_date_time.timestamp()
            if group_end_epoch == 0:
                group_end_epoch = current_entry.started_date_time.timestamp()
            if current_entry.started_date_time.timestamp() < group_start_epoch:
                group_start_epoch = current_entry.started_date_time.timestamp()
            if current_entry.started_date_time.timestamp() > group_end_epoch:
                group_end_epoch = current_entry.started_date_time.timestamp()
            group_static_time_millisec += current_entry.time

        group_non_static_time_millisec = 0
        for entry in entries_data['entries'][entry_group_name]['non-static']:
            current_entry: Entry = entry
            if group_start_epoch == 0:
                group_start_epoch = current_entry.started_date_time.timestamp()
            if group_end_epoch == 0:
                group_end_epoch = current_entry.started_date_time.timestamp()
            if current_entry.started_date_time.timestamp() < group_start_epoch:
                group_start_epoch = current_entry.started_date_time.timestamp()
            if current_entry.started_date_time.timestamp() > group_end_epoch:
                group_end_epoch = current_entry.started_date_time.timestamp()
            group_non_static_time_millisec += current_entry.time

        group_total_time_millisec = group_static_time_millisec + \
            group_non_static_time_millisec
        entries_data['entries'][entry_group_name]['group_total_time_millisec'] = group_total_time_millisec
        entries_data['entries'][entry_group_name]['group_static_time_millisec'] = group_static_time_millisec
        entries_data['entries'][entry_group_name]['group_non_static_time_millisec'] = group_non_static_time_millisec
        entries_data['entries'][entry_group_name]['group_start_datetime'] = group_start_epoch
        entries_data['entries'][entry_group_name]['group_end_datetime'] = group_end_epoch
        entries_data['entries'][entry_group_name]['group_time_difference_millisec'] = (
            group_end_epoch - group_start_epoch) * 1000
        group_think_time_millisec = entries_data['entries'][entry_group_name]['group_time_difference_millisec'] - \
            entries_data['entries'][entry_group_name]['group_total_time_millisec']
        if group_think_time_millisec > 0:
            entries_data['entries'][entry_group_name]['group_think_time_millisec'] = group_think_time_millisec
        else:
            entries_data['entries'][entry_group_name]['group_think_time_millisec'] = 0

    total_time_millisec = 0
    static_time_millisec = 0
    non_static_time_millisec = 0
    total_time_with_think_time = 0
    for entry_group_name in entries_data['entries']:
        total_time_millisec += entries_data['entries'][entry_group_name]['group_total_time_millisec']
        static_time_millisec += entries_data['entries'][entry_group_name]['group_static_time_millisec']
        non_static_time_millisec += entries_data['entries'][entry_group_name]['group_non_static_time_millisec']
        total_time_with_think_time += entries_data['entries'][entry_group_name]['group_total_time_millisec']
        total_time_with_think_time += entries_data['entries'][entry_group_name]['group_think_time_millisec']
    entries_data['total_time_millisec'] = total_time_millisec
    entries_data['static_time_millisec'] = static_time_millisec
    entries_data['non_static_time_millisec'] = non_static_time_millisec
    entries_data['total_time_with_think_time'] = total_time_with_think_time

    entries_data['minutes_on_one_iteration_with_think_time'] = entries_data['total_time_with_think_time'] / MILLISEC_IN_MUNUTE
    entries_data['throughput_in_minute_with_think_time'] = MILLISEC_IN_MUNUTE / \
        entries_data['total_time_with_think_time']
    entries_data['minutes_on_one_iteration_with_out_think_time'] = entries_data['total_time_millisec'] / \
        MILLISEC_IN_MUNUTE
    entries_data['throughput_in_minute_with_out_think_time'] = MILLISEC_IN_MUNUTE / \
        entries_data['total_time_millisec']
    entries_data['minutes_on_one_iteration_non_static'] = entries_data['non_static_time_millisec'] / MILLISEC_IN_MUNUTE
    entries_data['throughput_in_minute_non_static'] = MILLISEC_IN_MUNUTE / \
        entries_data['non_static_time_millisec']

    return entries_data


def write_entries_data(entries_data: dict, filename: str):
    with open(f'{filename}-groups-summary.csv', mode='w', encoding='UTF-8') as file:
        file.write(f'group_number,entry_group_name,group_total_time_millisec,group_static_time_millisec,group_non_static_time_millisec,group_start_datetime,group_end_datetime,group_time_difference_millisec,group_think_time\n')
        file.write(
            f"0,summary,{entries_data['total_time_millisec']},{entries_data['static_time_millisec']},{entries_data['non_static_time_millisec']},0,0,0,{entries_data['total_time_with_think_time']}\n")
        for entry_group_name in entries_data['entries']:
            group_number = entries_data['entries'][entry_group_name]['group_number']
            group_total_time_millisec = entries_data['entries'][entry_group_name]['group_total_time_millisec']
            group_static_time_millisec = entries_data['entries'][entry_group_name]['group_static_time_millisec']
            group_non_static_time_millisec = entries_data['entries'][
                entry_group_name]['group_non_static_time_millisec']
            group_start_datetime = entries_data['entries'][entry_group_name]['group_start_datetime']
            group_end_datetime = entries_data['entries'][entry_group_name]['group_end_datetime']
            group_time_difference_millisec = entries_data['entries'][
                entry_group_name]['group_time_difference_millisec']
            group_think_time = entries_data['entries'][entry_group_name]['group_think_time_millisec']
            file.write(f'{group_number},{entry_group_name},{group_total_time_millisec},{group_static_time_millisec},{group_non_static_time_millisec},{group_start_datetime},{group_end_datetime},{group_time_difference_millisec},{group_think_time}\n')

    with open(f'{filename}-results.json', mode='w', encoding='UTF-8') as file:
        entries_copy = copy.deepcopy(entries_data)
        del entries_copy['comments']
        del entries_copy['entries']
        del entries_copy['mime_types']
        json_data = json.dumps(entries_copy)
        file.write(json_data)


def main():
    filename = 'test5.har'
    with open(filename, encoding='utf-8-sig', errors='ignore') as file:
        json_data = json.load(file, strict=False)
        har_data = har_data_from_dict(json_data)
        entries = har_data.log.entries
        mime_types = get_mime_types(entries)
        static_mime_types = get_type_lists(mime_types)
        entries_by_comment = grouping_by_comment(entries, static_mime_types)
        entries_data = set_types(
            entries_by_comment, mime_types, static_mime_types)
        entries_data = set_times_in_entries(entries_data)
        write_entries_data(entries_data, filename)


if __name__ == "__main__":
    main()
