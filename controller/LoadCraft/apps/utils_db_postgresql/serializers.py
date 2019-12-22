from rest_framework import serializers
from .models import PostgresqlSettings, PgStatStatementsLine


class PostgresqlSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostgresqlSettings
        fields = ('label_id', 'dbname', 'username', 'password', 'host', 'port')


class DatabaseInformationSerializer(serializers.Serializer):
    user = serializers.CharField()
    dbname = serializers.CharField()
    host = serializers.CharField()
    port = serializers.IntegerField()
    tty = serializers.CharField()
    options = serializers.CharField()
    sslmode = serializers.CharField()
    sslcompression = serializers.CharField()
    krbsrvname = serializers.CharField()
    target_session_attrs = serializers.CharField()
    database_info = serializers.CharField()


class PgStatStatementsLineSerializer(serializers.Serializer):
    """https://www.postgresql.org/docs/9.4/pgstatstatements.html"""
    userid = serializers.IntegerField()
    dbid = serializers.IntegerField()
    queryid = serializers.CharField()
    query = serializers.CharField()
    calls = serializers.IntegerField()
    total_time = serializers.FloatField()
    min_time = serializers.FloatField()
    max_time = serializers.FloatField()
    mean_time = serializers.FloatField()
    stddev_time = serializers.FloatField()
    rows = serializers.IntegerField()
    shared_blks_hit = serializers.IntegerField()
    shared_blks_read = serializers.IntegerField()
    shared_blks_dirtied = serializers.IntegerField()
    shared_blks_written = serializers.IntegerField()
    local_blks_hit = serializers.IntegerField()
    local_blks_read = serializers.IntegerField()
    local_blks_dirtied = serializers.IntegerField()
    local_blks_written = serializers.IntegerField()
    temp_blks_read = serializers.IntegerField()
    temp_blks_written = serializers.IntegerField()
    blk_read_time = serializers.FloatField()
    blk_write_time = serializers.FloatField()
