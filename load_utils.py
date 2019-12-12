import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] %(levelname)-12s|process:%(process)-5s|thread:%(thread)-5s|funcName:%(funcName)s|message:%(message)s",
    handlers=[
        # logging.FileHandler('fileName.log'),
        logging.StreamHandler()
    ])

step_count = 10
users_per_step = 5
step_lenght = 600
ramp_up = 60
ramp_down = 0

if __name__ == "__main__":
    data = {
        'step_count': step_count,
        'users_per_step': users_per_step,
        'step_lenght': step_lenght,
        'ramp_up': ramp_up,
        'ramp_down': ramp_down,
        'steps': []
    }
    complete_test_time_in_sec = (
        step_lenght * step_count) + (ramp_up * step_count)
    data['completeTestTimeInSec'] = complete_test_time_in_sec

    for step_number in range(step_count):
        new_step = {
            'step_number': step_number + 1,
            'start_threads_count': users_per_step * step_count,
            'init_delay_sec': complete_test_time_in_sec / step_count * step_number,
            'start_up_time_sec': ramp_up,
            'ramp_down': ramp_down,
        }
        data['steps'].append(new_step)
    logging.info(f'data = {data}')
