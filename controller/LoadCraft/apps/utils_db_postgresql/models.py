from django.db import models
from django import forms


class PostgresqlSettings(models.Model):
    label_id = models.CharField(max_length=30, primary_key=True)
    dbname = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=150)
    host = models.CharField(max_length=150)
    port = models.IntegerField()

    def __str__(self):
        return f'{self.label_id} dbname:{self.dbname} username:{self.username}'


class DatabaseInformation:
    def __init__(self, user: str, dbname: str, host: str, port: int, tty: str, options: str,
                 sslmode: str, sslcompression: str, krbsrvname: str, target_session_attrs: str, database_info: str,):
        self.user = user
        self.dbname = dbname
        self.host = host
        self.port = port
        self.tty = tty
        self.options = options
        self.sslmode = sslmode
        self.sslcompression = sslcompression
        self.krbsrvname = krbsrvname
        self.target_session_attrs = target_session_attrs
        self.database_info = database_info


class PgStatStatementsLine:
    def __init__(self, userid: int, dbid: int, queryid: str, query: str, calls: int,
                 total_time: float, min_time: float, max_time: float, mean_time: float, stddev_time: float,
                 rows: int,
                 shared_blks_hit: int, shared_blks_read: int, shared_blks_dirtied: int, shared_blks_written: int,
                 local_blks_hit: int, local_blks_read: int, local_blks_dirtied: int, local_blks_written: int,
                 temp_blks_read: int, temp_blks_written: int, blk_read_time: float, blk_write_time: float):
        self.userid = userid
        self.dbid = dbid
        self.queryid = queryid
        self.query = query
        self.calls = calls
        self.total_time = total_time
        self.min_time = min_time
        self.max_time = max_time
        self.mean_time = mean_time
        self.stddev_time = stddev_time
        self.rows = rows
        self.shared_blks_hit = shared_blks_hit
        self.shared_blks_read = shared_blks_read
        self.shared_blks_dirtied = shared_blks_dirtied
        self.shared_blks_written = shared_blks_written
        self.local_blks_hit = local_blks_hit
        self.local_blks_read = local_blks_read
        self.local_blks_dirtied = local_blks_dirtied
        self.local_blks_written = local_blks_written
        self.temp_blks_read = temp_blks_read
        self.temp_blks_written = temp_blks_written
        self.blk_read_time = blk_read_time
        self.blk_write_time = blk_write_time

    def get_influxdb_string_format(self):
        pass

    def __str__(self):
        return f'query_id:{self.queryid} calls:{self.calls} total_time:{self.total_time}'
