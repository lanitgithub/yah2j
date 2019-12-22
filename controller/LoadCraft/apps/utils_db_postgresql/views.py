from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action, api_view, schema
from rest_framework.schemas import AutoSchema
from rest_framework import viewsets

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializers import PostgresqlSettingsSerializer
from .models import PostgresqlSettings

from .serializers import DatabaseInformationSerializer
from .models import DatabaseInformation

from .serializers import PgStatStatementsLine, PgStatStatementsLineSerializer

from typing import List

import psycopg2
import logging
import json

logger = logging.getLogger(__name__)


class PostgresqlSettingsView(viewsets.ModelViewSet):
    """This API allows you to interact, add, delete PostgreSQL configurations."""
    queryset = PostgresqlSettings.objects.all().order_by('label_id')
    serializer_class = PostgresqlSettingsSerializer

    @swagger_auto_schema(methods=['get'], responses={200: DatabaseInformationSerializer, 504: 'Database connection checked failed'})
    @action(methods=['GET'], detail=True)
    def check_connection(self, request, pk: PostgresqlSettings):
        """This method allows you to check the connection to the database."""
        logging.info(
            f'Checking database {pk} connection started...')

        response = None
        try:
            postgresql_setting: PostgresqlSettings = PostgresqlSettings.objects.get(
                pk=pk)
            logging.info(
                f'postgresql_setting{type(postgresql_setting)} = {postgresql_setting}')
            connection: psycopg2.extensions.connection = psycopg2.connect(user=postgresql_setting.username,
                                                                          password=postgresql_setting.password,
                                                                          host=postgresql_setting.host,
                                                                          port=postgresql_setting.port,
                                                                          database=postgresql_setting.dbname)

            logging.info(f'connection{type(connection)} = {connection}')
            database_info: dict = connection.get_dsn_parameters()
            cursor = connection.cursor()
            cursor.execute("SELECT version();")
            database_information = DatabaseInformation(user=database_info['user'], dbname=database_info['dbname'],
                                                       host=database_info['host'], port=database_info['port'],
                                                       tty=database_info['tty'], options=database_info['options'],
                                                       sslmode=database_info['sslmode'], sslcompression=database_info['sslcompression'],
                                                       krbsrvname=database_info['krbsrvname'], target_session_attrs=database_info[
                                                           'target_session_attrs'],
                                                       database_info=str(cursor.fetchone()).strip('[]'))
            logging.info(
                f'check_data_response {type(database_information)} = {database_information}')
            serializer_check_data_response = DatabaseInformationSerializer(
                database_information)
            response = HttpResponse(JSONRenderer().render(serializer_check_data_response.data),
                                    content_type="application/json; charset=utf-8")
            response.status_code = 200
        except (Exception, psycopg2.Error) as error:
            error_message = f'Error while connecting to PostgreSQL: {error}'
            response = HttpResponse(error_message)
            response.status_code = 503
            logging.error(error_message)
        finally:
            try:
                if(connection):
                    cursor.close()
                    connection.close()
            except (UnboundLocalError) as error:
                logging.warning('Database connection already closed')
            logging.info(
                f'Checking database {pk} connection completed')
            return response

    @swagger_auto_schema(manual_parameters=[openapi.Parameter(in_=openapi.IN_QUERY, type=openapi.TYPE_NUMBER, name='queryid', description="Query id from postgresql", required=True)], methods=['get'],
                         responses={200: PgStatStatementsLineSerializer, 500: 'There was a problem retrieving data from the database'})
    @action(methods=['GET'], detail=True)
    def get_query_by_id(self, request, pk: PostgresqlSettings):
        """This method allows you to get statistic about query by id."""
        queryid = request.GET.get('queryid')
        logging.info(f'queryid {type(queryid)} = {queryid}')
        logging.info(
            f'Getting query by id {queryid} from database {pk} started...')
        response = None
        try:
            postgresql_setting: PostgresqlSettings = PostgresqlSettings.objects.get(
                pk=pk)
            logging.info(
                f'postgresql_setting{type(postgresql_setting)} = {postgresql_setting}')
            connection: psycopg2.extensions.connection = psycopg2.connect(user=postgresql_setting.username,
                                                                          password=postgresql_setting.password,
                                                                          host=postgresql_setting.host,
                                                                          port=postgresql_setting.port,
                                                                          database=postgresql_setting.dbname)

            logging.info(f'connection{type(connection)} = {connection}')
            cursor = connection.cursor()
            cursor.execute(
                f"SELECT * FROM public.pg_stat_statements where queryid = {queryid};")

            row = cursor.fetchone()
            logging.info(f'row {type(row)} = {row}')
            pg_stat_statements_line = PgStatStatementsLine(userid=row[0], dbid=row[1], queryid=row[2], query=row[3], calls=row[4],
                                                           total_time=row[5], min_time=row[6],
                                                           max_time=row[7], mean_time=row[8], stddev_time=row[9],
                                                           rows=row[10], shared_blks_hit=row[11],
                                                           shared_blks_read=row[12],
                                                           shared_blks_dirtied=row[13], shared_blks_written=row[14],
                                                           local_blks_hit=row[15],
                                                           local_blks_read=row[16],
                                                           local_blks_dirtied=row[17], local_blks_written=row[18],
                                                           temp_blks_read=row[19], temp_blks_written=row[20], blk_read_time=row[21], blk_write_time=row[22])
            logging.info(
                f'pg_stat_statements_line {type(pg_stat_statements_line)} = {pg_stat_statements_line}')
            serializer = PgStatStatementsLineSerializer(
                pg_stat_statements_line)
            response = HttpResponse(JSONRenderer().render(serializer.data),
                                    content_type="application/json; charset=utf-8")
            response.status_code = 200
        except (Exception, psycopg2.Error) as error:
            error_message = f'Error while connecting to PostgreSQL: {error}'
            response = HttpResponse(error_message)
            response.status_code = 503
            logging.error(error_message)
        finally:
            try:
                if(connection):
                    cursor.close()
                    connection.close()
            except (UnboundLocalError) as error:
                logging.warning('Database connection already closed')
            logging.info(
                f'Getting query by id {queryid} from database {pk} completed')
            return response

    @swagger_auto_schema(methods=['get'], responses={200: PgStatStatementsLineSerializer(many=True), 500: 'There was a problem retrieving data from the database'})
    @action(methods=['GET'], detail=True)
    def pg_stat_statements_collect_all(self, request, pk: PostgresqlSettings):
        """This method allows you to get all pg_stat_statements statistic."""
        logging.info(
            f'Getting pg_stat_statements statistic from database {pk} started...')
        response = None
        try:
            postgresql_setting: PostgresqlSettings = PostgresqlSettings.objects.get(
                pk=pk)
            logging.info(
                f'postgresql_setting{type(postgresql_setting)} = {postgresql_setting}')
            connection: psycopg2.extensions.connection = psycopg2.connect(user=postgresql_setting.username,
                                                                          password=postgresql_setting.password,
                                                                          host=postgresql_setting.host,
                                                                          port=postgresql_setting.port,
                                                                          database=postgresql_setting.dbname)

            logging.info(f'connection{type(connection)} = {connection}')
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM public.pg_stat_statements;")
            pg_stat_statements_lines: List[PgStatStatementsLine] = []
            for row in cursor.fetchall():
                logging.info(f'row {type(row)} = {row}')
                pg_stat_statements_line = PgStatStatementsLine(userid=row[0], dbid=row[1], queryid=row[2], query=row[3],
                                                               calls=row[4],
                                                               total_time=row[5], min_time=row[6],
                                                               max_time=row[7], mean_time=row[8], stddev_time=row[9],
                                                               rows=row[10], shared_blks_hit=row[11],
                                                               shared_blks_read=row[12],
                                                               shared_blks_dirtied=row[13], shared_blks_written=row[14],
                                                               local_blks_hit=row[15],
                                                               local_blks_read=row[16],
                                                               local_blks_dirtied=row[17], local_blks_written=row[18],
                                                               temp_blks_read=row[19], temp_blks_written=row[20], blk_read_time=row[21], blk_write_time=row[22])
                logging.info(
                    f'pg_stat_statements_line {type(pg_stat_statements_line)} = {pg_stat_statements_line}')
                pg_stat_statements_lines.append(pg_stat_statements_line)
            serializer = PgStatStatementsLineSerializer(
                pg_stat_statements_lines, many=True)
            response = HttpResponse(JSONRenderer().render(serializer.data),
                                    content_type="application/json; charset=utf-8")
            response.status_code = 200
        except (Exception, psycopg2.Error) as error:
            error_message = f'Error while connecting to PostgreSQL: {error}'
            response = HttpResponse(error_message)
            response.status_code = 503
            logging.error(error_message)
        finally:
            try:
                if(connection):
                    cursor.close()
                    connection.close()
            except (UnboundLocalError) as error:
                logging.warning('Database connection already closed')
            logging.info(
                f'Getting pg_stat_statements statistic from database {pk} completed')
            return response

    @swagger_auto_schema(methods=['get'], responses={204: 'Resetting pg_stat_statements for {pk} completed', 504: 'There was a problem to reset pg_stat_statements'})
    @action(methods=['GET'], detail=True)
    def pg_stat_statements_reset(self, request, pk: PostgresqlSettings):
        """This method allows you to reset pg_stat_statements statistic"""
        logging.info(
            f'Resetting pg_stat_statements for {pk} started...')
        response = None
        try:
            postgresql_setting: PostgresqlSettings = PostgresqlSettings.objects.get(
                pk=pk)
            logging.info(
                f'postgresql_setting{type(postgresql_setting)} = {postgresql_setting}')
            connection: psycopg2.extensions.connection = psycopg2.connect(user=postgresql_setting.username,
                                                                          password=postgresql_setting.password,
                                                                          host=postgresql_setting.host,
                                                                          port=postgresql_setting.port,
                                                                          database=postgresql_setting.dbname)
            logging.info(f'connection{type(connection)} = {connection}')
            cursor = connection.cursor()
            cursor.execute("SELECT public.pg_stat_statements_reset();")
            response = HttpResponse()
            response.status_code = 204
        except (Exception, psycopg2.Error) as error:
            error_message = f'Error while connecting to PostgreSQL: {error}'
            response = HttpResponse(error_message)
            response.status_code = 503
            logging.error(error_message)
        finally:
            try:
                if(connection):
                    cursor.close()
                    connection.close()
            except (UnboundLocalError) as error:
                logging.warning('Database connection already closed')
            logging.info(f'Resetting pg_stat_statements for {pk} completed')
            return response


# def (request):
#     return HttpResponse('')


# def pg_stat_statements_collect_json_format(request):
#     return HttpResponse('')


# def pg_stat_activity_collect_json_format(request):
#     return HttpResponse('')


# def run_custom_query(request):
#     return HttpResponse('')


# test_param1 = openapi.Parameter(
#     in_=openapi.IN_QUERY, type=openapi.TYPE_BOOLEAN, name='test1', description="test manual param", )
# test_param2 = openapi.Parameter(
#     in_=openapi.IN_QUERY, type=openapi.TYPE_STRING, name='test2', description="test manual param", enum=['qwerty', 'asdfgh', 'cxvb'])
# test_param3 = openapi.Parameter(
#     in_=openapi.IN_QUERY, type=openapi.TYPE_NUMBER, name='test3', description="test manual param", )
# test_param3 = openapi.Parameter(
#     in_=openapi.IN_PATH,  type=openapi.TYPE_NUMBER, name='test4', description="test manual param", )


# @swagger_auto_schema(manual_parameters=[test_param1, test_param2, test_param3], methods=['put', 'post'], responses={201: PgStatStatementsDataSerializer(many=True), 404: 'slug not found'})
# @api_view(['put', 'post'])
# def cancel_payments(request, postgresql_settings_label_id: str, pk: int):
#     """
#     Returns a list of all **active** accounts in the system.

#     For more details on how accounts are activated please [see here][ref].

#     [ref]: http://example.com/activating-accounts
#     """
#     logging.info('cancel_payments started...')

#     var_name = 'qweasdasdsad'
#     logging.info(f'var_name{type(var_name)} = {var_name}')

#     logging.info('cancel_payments completed')
#     var_name = PgStatStatementsDataSerializer.create([])
#     #pgdata = PgStatStatementsDataSerializer([PgStatStatementsLineSerializer(1,1,1,'qwe',1,1.1,1.1,1.1,1.1,1.1,1,1,1,1,1,1,1,1,1,1,1,1.1,1.1)])
#     return var_name


# @swagger_auto_schema(manual_parameters=[test_param1, test_param2, test_param3], methods=['put', 'post'], responses={201: PgStatStatementsLineSerializer, 404: 'slug not found'})
# @api_view(['put', 'post'])
# def cancel_payments(request: Request):
#     """
#     Returns a list of all **active** accounts in the system.

#     For more details on how accounts are activated please [see here][ref].

#     [ref]: http://example.com/activating-accounts
#     """
#     logging.info('cancel_payments started...')

#     logging.info(f'request {type(request)} = {request}')
#     logging.info('cancel_payments completed')
#     data = [PgStatStatementsLine(1, 1, 1, 'qwe', 1, 1.1, 1.1, 1.1,
#                                  1.1, 1.1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1.1, 1.1),
#             PgStatStatementsLine(1, 1, 1, 'asdqwe', 1, 1.1, 1.1, 1.1,
#                                  1.1, 1.1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1.1, 1.1), ]
#     ser_data = PgStatStatementsLineSerializer(data, many=True)

#     return HttpResponse(JSONRenderer().render(ser_data.data))
