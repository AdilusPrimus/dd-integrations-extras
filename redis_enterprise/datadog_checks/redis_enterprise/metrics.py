# enterprise metrics use the namespace 'rdse'
REDIS_CLUSTER = {'cluster_shards_limit': 'cluster_shards_limit'}

REDIS_DATABASE = {
    'bdb_avg_latency': 'bdb_avg_latency',
    'bdb_avg_latency_max': 'bdb_avg_latency_max',
    'bdb_avg_read_latency': 'bdb_avg_read_latency',
    'bdb_avg_read_latency_max': 'bdb_avg_read_latency_max',
    'bdb_avg_write_latency': 'bdb_avg_write_latency',
    'bdb_avg_write_latency_max': 'bdb_avg_write_latency_max',
    'bdb_conns': 'bdb_conns',
    'bdb_egress_bytes': 'bdb_egress_bytes',
    'bdb_egress_bytes_max': 'bdb_egress_bytes_max',
    'bdb_evicted_objects': 'bdb_evicted_objects',
    'bdb_evicted_objects_max': 'bdb_evicted_objects_max',
    'bdb_expired_objects': 'bdb_expired_objects',
    'bdb_expired_objects_max': 'bdb_expired_objects_max',
    'bdb_fork_cpu_system': 'bdb_fork_cpu_system',
    'bdb_fork_cpu_system_max': 'bdb_fork_cpu_system_max',
    'bdb_fork_cpu_user': 'bdb_fork_cpu_user',
    'bdb_fork_cpu_user_max': 'bdb_fork_cpu_user_max',
    'bdb_ingress_bytes': 'bdb_ingress_bytes',
    'bdb_ingress_bytes_max': 'bdb_ingress_bytes_max',
    'bdb_instantaneous_ops_per_sec': 'bdb_instantaneous_ops_per_sec',
    'bdb_main_thread_cpu_system': 'bdb_main_thread_cpu_system',
    'bdb_main_thread_cpu_system_max': 'bdb_main_thread_cpu_system_max',
    'bdb_main_thread_cpu_user': 'bdb_main_thread_cpu_user',
    'bdb_main_thread_cpu_user_max': 'bdb_main_thread_cpu_user_max',
    'bdb_mem_frag_ratio': 'bdb_mem_frag_ratio',
    'bdb_mem_size_lua': 'bdb_mem_size_lua',
    'bdb_memory_limit': 'bdb_memory_limit',
    'bdb_monitor_sessions_count': 'bdb_monitor_sessions_count',
    'bdb_no_of_keys': 'bdb_no_of_keys',
    'bdb_other_req': 'bdb_other_req',
    'bdb_other_req_max': 'bdb_other_req_max',
    'bdb_other_res': 'bdb_other_res',
    'bdb_other_res_max': 'bdb_other_res_max',
    'bdb_pubsub_channels': 'bdb_pubsub_channels',
    'bdb_pubsub_channels_max': 'bdb_pubsub_channels_max',
    'bdb_pubsub_patterns': 'bdb_pubsub_patterns',
    'bdb_pubsub_patterns_max': 'bdb_pubsub_patterns_max',
    'bdb_read_hits': 'bdb_read_hits',
    'bdb_read_hits_max': 'bdb_read_hits_max',
    'bdb_read_misses': 'bdb_read_misses',
    'bdb_read_misses_max': 'bdb_read_misses_max',
    'bdb_read_req': 'bdb_read_req',
    'bdb_read_req_max': 'bdb_read_req_max',
    'bdb_read_res': 'bdb_read_res',
    'bdb_read_res_max': 'bdb_read_res_max',
    'bdb_shard_cpu_system': 'bdb_shard_cpu_system',
    'bdb_shard_cpu_system_max': 'bdb_shard_cpu_system_max',
    'bdb_shard_cpu_user': 'bdb_shard_cpu_user',
    'bdb_shard_cpu_user_max': 'bdb_shard_cpu_user_max',
    'bdb_total_connections_received': 'bdb_total_connections_received',
    'bdb_total_connections_received_max': 'bdb_total_connections_received_max',
    'bdb_total_req': 'bdb_total_req',
    'bdb_total_req_max': 'bdb_total_req_max',
    'bdb_total_res': 'bdb_total_res',
    'bdb_total_res_max': 'bdb_total_res_max',
    'bdb_up': 'bdb_up',
    'bdb_used_memory': 'bdb_used_memory',
    'bdb_write_hits': 'bdb_write_hits',
    'bdb_write_hits_max': 'bdb_write_hits_max',
    'bdb_write_misses': 'bdb_write_misses',
    'bdb_write_misses_max': 'bdb_write_misses_max',
    'bdb_write_req': 'bdb_write_req',
    'bdb_write_req_max': 'bdb_write_req_max',
    'bdb_write_res': 'bdb_write_res',
    'bdb_write_res_max': 'bdb_write_res_max',
}

REDIS_NODE = {
    'namedprocess_namegroup_thread_cpu_seconds_total': {
        'name': 'namedprocess_namegroup_thread_cpu_seconds_total',
        'type': 'gauge',
    },
    'no_of_expires': 'no_of_expires',
    'node_available_memory': 'node_available_memory',
    'node_available_memory_no_overbooking': 'node_available_memory_no_overbooking',
    'node_avg_latency': 'node_avg_latency',
    'node_cert_expiration_seconds': {
        'name': 'node_cert_expiration_seconds',
        'type': 'gauge',
    },
    'node_conns': 'node_conns',
    'node_cpu_idle': 'node_cpu_idle',
    'node_cpu_idle_max': 'node_cpu_idle_max',
    'node_cpu_idle_median': 'node_cpu_idle_median',
    'node_cpu_idle_min': 'node_cpu_idle_min',
    'node_cpu_iowait': 'node_cpu_iowait',
    'node_cpu_iowait_max': 'node_cpu_iowait_max',
    'node_cpu_iowait_median': 'node_cpu_iowait_median',
    'node_cpu_iowait_min': 'node_cpu_iowait_min',
    'node_cpu_irqs': 'node_cpu_irqs',
    'node_cpu_irqs_max': 'node_cpu_irqs_max',
    'node_cpu_irqs_median': 'node_cpu_irqs_median',
    'node_cpu_irqs_min': 'node_cpu_irqs_min',
    'node_cpu_nice': 'node_cpu_nice',
    'node_cpu_nice_max': 'node_cpu_nice_max',
    'node_cpu_nice_median': 'node_cpu_nice_median',
    'node_cpu_nice_min': 'node_cpu_nice_min',
    'node_cpu_steal': 'node_cpu_steal',
    'node_cpu_steal_max': 'node_cpu_steal_max',
    'node_cpu_steal_median': 'node_cpu_steal_median',
    'node_cpu_steal_min': 'node_cpu_steal_min',
    'node_cpu_system': 'node_cpu_system',
    'node_cpu_system_max': 'node_cpu_system_max',
    'node_cpu_system_median': 'node_cpu_system_median',
    'node_cpu_system_min': 'node_cpu_system_min',
    'node_cpu_user': 'node_cpu_user',
    'node_cpu_user_max': 'node_cpu_user_max',
    'node_cpu_user_median': 'node_cpu_user_median',
    'node_cpu_user_min': 'node_cpu_user_min',
    'node_cur_aof_rewrites': 'node_cur_aof_rewrites',
    'node_egress_bytes': 'node_egress_bytes',
    'node_egress_bytes_max': 'node_egress_bytes_max',
    'node_egress_bytes_median': 'node_egress_bytes_median',
    'node_egress_bytes_min': 'node_egress_bytes_min',
    'node_ephemeral_storage_avail': 'node_ephemeral_storage_avail',
    'node_ephemeral_storage_free': 'node_ephemeral_storage_free',
    'node_free_memory': 'node_free_memory',
    'node_ingress_bytes': 'node_ingress_bytes',
    'node_ingress_bytes_max': 'node_ingress_bytes_max',
    'node_ingress_bytes_median': 'node_ingress_bytes_median',
    'node_ingress_bytes_min': 'node_ingress_bytes_min',
    'node_persistent_storage_avail': 'node_persistent_storage_avail',
    'node_persistent_storage_free': 'node_persistent_storage_free',
    'node_provisional_memory': 'node_provisional_memory',
    'node_provisional_memory_no_overbooking': 'node_provisional_memory_no_overbooking',
    'node_total_req': 'node_total_req',
    'node_up': {
        'name': 'node_up',
        'type': 'gauge',
    },
}

REDIS_SHARD = {
    'redis_active_defrag_running': {'name': 'redis_active_defrag_running', 'type': 'rate'},
    'redis_allocator_active': {'name': 'redis_allocator_active', 'type': 'gauge'},
    'redis_allocator_allocated': {'name': 'redis_allocator_allocated', 'type': 'gauge'},
    'redis_allocator_resident': {'name': 'redis_allocator_resident', 'type': 'gauge'},
    'redis_aof_last_cow_size': {'name': 'redis_aof_last_cow_size', 'type': 'gauge'},
    'redis_aof_rewrite_in_progress': {'name': 'redis_aof_rewrite_in_progress', 'type': 'gauge'},
    'redis_aof_rewrites': {'name': 'redis_aof_rewrites', 'type': 'gauge'},
    'redis_aof_delayed_fsync': {'name': 'redis_aof_delayed_fsync', 'type': 'gauge'},
    'redis_blocked_clients': {'name': 'redis_blocked_clients', 'type': 'gauge'},
    'redis_blocking_reads': {'name': 'redis_blocking_reads', 'type': 'gauge'},
    'redis_blocking_writes': {'name': 'redis_blocking_writes', 'type': 'gauge'},
    'redis_connected_clients': {'name': 'redis_connected_clients', 'type': 'gauge'},
    'redis_connected_slaves': {'name': 'redis_connected_slaves', 'type': 'gauge'},
    'redis_db0_avg_ttl': {'name': 'redis_db0_avg_ttl', 'type': 'rate'},
    'redis_db0_expires': {'name': 'redis_db0_expires', 'type': 'gauge'},
    'redis_db0_keys': {'name': 'redis_db0_keys', 'type': 'gauge'},
    'redis_evicted_keys': {'name': 'redis_evicted_keys', 'type': 'gauge'},
    'redis_expire_cycle_cpu_milliseconds': {'name': 'redis_expire_cycle_cpu_milliseconds', 'type': 'gauge'},
    'redis_expired_keys': {'name': 'redis_expired_keys', 'type': 'gauge'},
    'redis_forwarding_state': {'name': 'redis_forwarding_state', 'type': 'gauge'},
    'redis_keys_trimmed': {'name': 'redis_keys_trimmed', 'type': 'gauge'},
    'redis_keyspace_read_hits': {'name': 'redis_keyspace_read_hits', 'type': 'gauge'},
    'redis_keyspace_read_misses': {'name': 'redis_keyspace_read_misses', 'type': 'gauge'},
    'redis_keyspace_write_hits': {'name': 'redis_keyspace_write_hits', 'type': 'gauge'},
    'redis_keyspace_write_misses': {'name': 'redis_keyspace_write_misses', 'type': 'gauge'},
    'redis_master_link_status': {'name': 'redis_master_link_status', 'type': 'gauge'},
    'redis_master_repl_offset': {'name': 'redis_master_repl_offset', 'type': 'gauge'},
    'redis_master_sync_in_progress': {'name': 'redis_master_sync_in_progress', 'type': 'gauge'},
    'redis_max_process_mem': {'name': 'redis_max_process_mem', 'type': 'gauge'},
    'redis_maxmemory': {'name': 'redis_maxmemory', 'type': 'gauge'},
    'redis_mem_aof_buffer': {'name': 'redis_mem_aof_buffer', 'type': 'gauge'},
    'redis_mem_clients_normal': {'name': 'redis_mem_clients_normal', 'type': 'gauge'},
    'redis_mem_clients_slaves': {'name': 'redis_mem_clients_slaves', 'type': 'gauge'},
    'redis_mem_fragmentation_ratio': {'name': 'redis_mem_fragmentation_ratio', 'type': 'histogram'},
    'redis_mem_not_counted_for_evict': {'name': 'redis_mem_not_counted_for_evict', 'type': 'gauge'},
    'redis_mem_replication_backlog': {'name': 'redis_mem_replication_backlog', 'type': 'gauge'},
    'redis_module_fork_in_progress': {'name': 'redis_module_fork_in_progress', 'type': 'gauge'},
    'redis_process_cpu_system_seconds_total': {'name': 'redis_process_cpu_system_seconds_total', 'type': 'gauge'},
    'redis_process_cpu_usage_percent': {'name': 'redis_process_cpu_usage_percent', 'type': 'gauge'},
    'redis_process_cpu_user_seconds_total': {'name': 'redis_process_cpu_user_seconds_total', 'type': 'gauge'},
    'redis_process_main_thread_cpu_system_seconds_total': {
        'name': 'redis_process_main_thread_cpu_system_seconds_total',
        'type': 'gauge',
    },
    'redis_process_main_thread_cpu_user_seconds_total': {
        'name': 'redis_process_main_thread_cpu_user_seconds_total',
        'type': 'gauge',
    },
    'redis_process_max_fds': {'name': 'redis_process_max_fds', 'type': 'gauge'},
    'redis_process_open_fds': {'name': 'redis_process_open_fds', 'type': 'gauge'},
    'redis_process_resident_memory_bytes': {'name': 'redis_process_resident_memory_bytes', 'type': 'gauge'},
    'redis_process_start_time_seconds': {'name': 'redis_process_start_time_seconds', 'type': 'gauge'},
    'redis_process_virtual_memory_bytes': {'name': 'redis_process_virtual_memory_bytes', 'type': 'gauge'},
    'redis_rdb_bgsave_in_progress': {'name': 'redis_rdb_bgsave_in_progress', 'type': 'gauge'},
    'redis_rdb_last_cow_size': {'name': 'redis_rdb_last_cow_size', 'type': 'gauge'},
    'redis_rdb_saves': {'name': 'redis_rdb_saves', 'type': 'gauge'},
    'redis_repl_touch_bytes': {'name': 'redis_repl_touch_bytes', 'type': 'gauge'},
    'redis_total_commands_processed': {'name': 'redis_total_commands_processed', 'type': 'gauge'},
    'redis_total_connections_received': {'name': 'redis_total_connections_received', 'type': 'gauge'},
    'redis_total_net_input_bytes': {'name': 'redis_total_net_input_bytes', 'type': 'gauge'},
    'redis_total_net_output_bytes': {'name': 'redis_total_net_output_bytes', 'type': 'gauge'},
    'redis_up': {'name': 'redis_up', 'type': 'gauge'},
    'redis_used_disk': {'name': 'redis_used_disk', 'type': 'gauge'},
    'redis_used_memory': {'name': 'redis_used_memory', 'type': 'gauge'},
}

REDIS_REPLICATION = {
    'bdb_crdt_syncer_ingress_bytes': {'name': 'bdb_crdt_syncer_ingress_bytes', 'type': 'gauge'},
    'bdb_crdt_syncer_ingress_bytes_decompressed': {
        'name': 'bdb_crdt_syncer_ingress_bytes_decompressed',
        'type': 'gauge',
    },
    'bdb_crdt_syncer_local_ingress_lag_time': {'name': 'bdb_crdt_syncer_local_ingress_lag_time', 'type': 'gauge'},
    'bdb_crdt_syncer_status': {'name': 'bdb_crdt_syncer_status', 'type': 'gauge'},
    'bdb_crdt_syncer_egress_bytes': {'name': 'bdb_crdt_syncer_egress_bytes', 'type': 'gauge'},
    'bdb_crdt_syncer_egress_bytes_decompressed': {
        'name': 'bdb_crdt_syncer_egress_bytes_decompressed',
        'type': 'gauge',
    },
    'bdb_crdt_syncer_egress_bytes_decompressed_max': {
        'name': 'bdb_crdt_syncer_egress_bytes_decompressed_max',
        'type': 'gauge',
    },
    'bdb_crdt_syncer_egress_bytes_max': {'name': 'bdb_crdt_syncer_egress_bytes_max', 'type': 'gauge'},
    'bdb_replicaof_syncer_ingress_bytes': {'name': 'bdb_replicaof_syncer_ingress_bytes', 'type': 'gauge'},
    'bdb_replicaof_syncer_ingress_bytes_decompressed': {
        'name': 'bdb_replicaof_syncer_ingress_bytes_decompressed',
        'type': 'gauge',
    },
    'bdb_replicaof_syncer_local_ingress_lag_time': {
        'name': 'bdb_replicaof_syncer_local_ingress_lag_time',
        'type': 'gauge',
    },
    'bdb_replicaof_syncer_status': {'name': 'bdb_replicaof_syncer_status', 'type': 'gauge'},
}

REDIS_SHARD_REPLICATION = {
    'redis_crdt_backlog_histlen': {'name': 'redis_crdt_backlog_histlen', 'type': 'gauge'},
    'redis_crdt_backlog_idx': {'name': 'redis_crdt_backlog_idx', 'type': 'gauge'},
    'redis_crdt_backlog_master_offset': {'name': 'redis_crdt_backlog_master_offset', 'type': 'gauge'},
    'redis_crdt_backlog_offset': {'name': 'redis_crdt_backlog_offset', 'type': 'gauge'},
    'redis_crdt_backlog_refs': {'name': 'redis_crdt_backlog_refs', 'type': 'gauge'},
    'redis_crdt_backlog_size': {'name': 'redis_crdt_backlog_size', 'type': 'gauge'},
    'redis_crdt_clock': {'name': 'redis_crdt_clock', 'type': 'gauge'},
    'redis_crdt_effect_reqs': {'name': 'redis_crdt_effect_reqs', 'type': 'gauge'},
    'redis_crdt_gc_attempted': {'name': 'redis_crdt_gc_attempted', 'type': 'gauge'},
    'redis_crdt_gc_collected': {'name': 'redis_crdt_gc_collected', 'type': 'gauge'},
    'redis_crdt_gc_elements_attempted': {'name': 'redis_crdt_gc_elements_attempted', 'type': 'gauge'},
    'redis_crdt_gc_elements_collected': {'name': 'redis_crdt_gc_elements_collected', 'type': 'gauge'},
    'redis_crdt_gc_pending': {'name': 'redis_crdt_gc_pending', 'type': 'gauge'},
    'redis_crdt_gc_skipped': {'name': 'redis_crdt_gc_skipped', 'type': 'gauge'},
    'redis_crdt_key_headers': {'name': 'redis_crdt_key_headers', 'type': 'gauge'},
    'redis_crdt_list_trimmed_vertices': {'name': 'redis_crdt_list_trimmed_vertices', 'type': 'gauge'},
    'redis_crdt_merge_reqs': {'name': 'redis_crdt_merge_reqs', 'type': 'gauge'},
    'redis_crdt_oom_latch': {'name': 'redis_crdt_oom_latch', 'type': 'gauge'},
    'redis_crdt_ovc_filtered_effect_reqs': {'name': 'redis_crdt_ovc_filtered_effect_reqs', 'type': 'gauge'},
    'redis_crdt_peer_dst_id': {'name': 'redis_crdt_peer_dst_id', 'type': 'gauge'},
    'redis_crdt_peer_id': {'name': 'redis_crdt_peer_id', 'type': 'gauge'},
    'redis_crdt_peer_lag': {'name': 'redis_crdt_peer_lag', 'type': 'gauge'},
    'redis_crdt_peer_offset': {'name': 'redis_crdt_peer_offset', 'type': 'gauge'},
    'redis_crdt_peer_peer_state': {'name': 'redis_crdt_peer_peer_state', 'type': 'gauge'},
    'redis_crdt_pending_list_trimmed_vertices': {'name': 'redis_crdt_pending_list_trimmed_vertices', 'type': 'gauge'},
    'redis_crdt_raw_dbsize': {'name': 'redis_crdt_raw_dbsize', 'type': 'gauge'},
    'redis_crdt_replica_config_version': {'name': 'redis_crdt_replica_config_version', 'type': 'gauge'},
    'redis_crdt_replica_max_ops_lag': {'name': 'redis_crdt_replica_max_ops_lag', 'type': 'gauge'},
    'redis_crdt_replica_min_ops_lag': {'name': 'redis_crdt_replica_min_ops_lag', 'type': 'gauge'},
    'redis_crdt_replica_shards': {'name': 'redis_crdt_replica_shards', 'type': 'gauge'},
    'redis_crdt_replica_slot_coverage_by_any_ovc': {
        'name': 'redis_crdt_replica_slot_coverage_by_any_ovc',
        'type': 'gauge',
    },
    'redis_crdt_replica_slot_coverage_by_only_ovc': {
        'name': 'redis_crdt_replica_slot_coverage_by_only_ovc',
        'type': 'gauge',
    },
    'redis_crdt_replica_slots': {'name': 'redis_crdt_replica_slots', 'type': 'gauge'},
    'redis_crdt_stale_replica': {'name': 'redis_crdt_stale_replica', 'type': 'gauge'},
    'redis_crdt_ts_key_headers': {'name': 'redis_crdt_ts_key_headers', 'type': 'gauge'},
}

REDIS_PROXY = {
    'dmcproxy_process_cpu_system_seconds_total': {'name': 'dmcproxy_process_cpu_system_seconds_total', 'type': 'gauge'},
    'dmcproxy_process_cpu_usage_percent': {'name': 'dmcproxy_process_cpu_usage_percent', 'type': 'gauge'},
    'dmcproxy_process_cpu_user_seconds_total': {'name': 'dmcproxy_process_cpu_user_seconds_total', 'type': 'gauge'},
    'dmcproxy_process_main_thread_cpu_system_seconds_total': {
        'name': 'dmcproxy_process_main_thread_cpu_system_seconds_total',
        'type': 'gauge',
    },
    'dmcproxy_process_main_thread_cpu_user_seconds_total': {
        'name': 'dmcproxy_process_main_thread_cpu_user_seconds_total',
        'type': 'gauge',
    },
    'dmcproxy_process_max_fds': {'name': 'dmcproxy_process_max_fds', 'type': 'gauge'},
    'dmcproxy_process_open_fds': {'name': 'dmcproxy_process_open_fds', 'type': 'gauge'},
    'dmcproxy_process_resident_memory_bytes': {'name': 'dmcproxy_process_resident_memory_bytes', 'type': 'gauge'},
    'dmcproxy_process_start_time_seconds': {'name': 'dmcproxy_process_start_time_seconds', 'type': 'gauge'},
    'dmcproxy_process_virtual_memory_bytes': {'name': 'dmcproxy_process_virtual_memory_bytes', 'type': 'gauge'},
}

REDIS_LISTENER = {
    'listener_acc_latency': {'name': 'listener_acc_latency_total', 'type': 'gauge'},
    'listener_acc_latency_max': {'name': 'listener_acc_latency_max_total', 'type': 'gauge'},
    'listener_acc_other_latency': {'name': 'listener_acc_other_latency', 'type': 'gauge'},
    'listener_acc_other_latency_max': {'name': 'listener_acc_other_latency_max', 'type': 'gauge'},
    'listener_acc_read_latency': {'name': 'listener_acc_read_latency', 'type': 'gauge'},
    'listener_acc_read_latency_max': {'name': 'listener_acc_read_latency_max', 'type': 'gauge'},
    'listener_acc_write_latency': {'name': 'listener_acc_write_latency', 'type': 'gauge'},
    'listener_acc_write_latency_max': {'name': 'listener_acc_write_latency_max', 'type': 'gauge'},
    'listener_auth_cmds': {'name': 'listener_auth_cmds', 'type': 'gauge'},
    'listener_auth_cmds_max': {'name': 'listener_auth_cmds_max', 'type': 'gauge'},
    'listener_auth_errors': {'name': 'listener_auth_errors', 'type': 'gauge'},
    'listener_auth_errors_max': {'name': 'listener_auth_errors_max', 'type': 'gauge'},
    'listener_cmd_flush': {'name': 'listener_cmd_flush', 'type': 'gauge'},
    'listener_cmd_flush_max': {'name': 'listener_cmd_flush_max', 'type': 'gauge'},
    'listener_cmd_get': {'name': 'listener_cmd_get', 'type': 'gauge'},
    'listener_cmd_get_max': {'name': 'listener_cmd_get_max', 'type': 'gauge'},
    'listener_cmd_set': {'name': 'listener_cmd_set', 'type': 'gauge'},
    'listener_cmd_set_max': {'name': 'listener_cmd_set_max', 'type': 'gauge'},
    'listener_cmd_touch': {'name': 'listener_cmd_touch', 'type': 'gauge'},
    'listener_cmd_touch_max': {'name': 'listener_cmd_touch_max', 'type': 'gauge'},
    'listener_conns': {'name': 'listener_conns', 'type': 'gauge'},
    'listener_egress_bytes': {'name': 'listener_egress_bytes', 'type': 'gauge'},
    'listener_egress_bytes_max': {'name': 'listener_egress_bytes_max', 'type': 'gauge'},
    'listener_ingress_bytes': {'name': 'listener_ingress_bytes', 'type': 'gauge'},
    'listener_ingress_bytes_max': {'name': 'listener_ingress_bytes_max', 'type': 'gauge'},
    'listener_last_req_time': {'name': 'listener_last_req_time', 'type': 'gauge'},
    'listener_last_res_time': {'name': 'listener_last_res_time', 'type': 'gauge'},
    'listener_max_connections_exceeded': {'name': 'listener_max_connections_exceeded', 'type': 'gauge'},
    'listener_max_connections_exceeded_max': {'name': 'listener_max_connections_exceeded_max', 'type': 'gauge'},
    'listener_monitor_sessions_count': {'name': 'listener_monitor_sessions_count', 'type': 'gauge'},
    'listener_other_req': {'name': 'listener_other_req', 'type': 'gauge'},
    'listener_other_req_max': {'name': 'listener_other_req_max', 'type': 'gauge'},
    'listener_other_res': {'name': 'listener_other_res', 'type': 'gauge'},
    'listener_other_res_max': {'name': 'listener_other_res_max', 'type': 'gauge'},
    'listener_other_started_res': {'name': 'listener_other_started_res', 'type': 'gauge'},
    'listener_other_started_res_max': {'name': 'listener_other_started_res_max', 'type': 'gauge'},
    'listener_read_req': {'name': 'listener_read_req', 'type': 'gauge'},
    'listener_read_req_max': {'name': 'listener_read_req_max', 'type': 'gauge'},
    'listener_read_res': {'name': 'listener_read_res', 'type': 'gauge'},
    'listener_read_res_max': {'name': 'listener_read_res_max', 'type': 'gauge'},
    'listener_read_started_res': {'name': 'listener_read_started_res', 'type': 'gauge'},
    'listener_read_started_res_max': {'name': 'listener_read_started_res_max', 'type': 'gauge'},
    'listener_total_connections_received': {'name': 'listener_total_connections_received', 'type': 'gauge'},
    'listener_total_connections_received_max': {'name': 'listener_total_connections_received_max', 'type': 'gauge'},
    'listener_total_req': {'name': 'listener_total_req', 'type': 'gauge'},
    'listener_total_req_max': {'name': 'listener_total_req_max', 'type': 'gauge'},
    'listener_total_res': {'name': 'listener_total_res', 'type': 'gauge'},
    'listener_total_res_max': {'name': 'listener_total_res_max', 'type': 'gauge'},
    'listener_total_started_res': {'name': 'listener_total_started_res', 'type': 'gauge'},
    'listener_total_started_res_max': {'name': 'listener_total_started_res_max', 'type': 'gauge'},
    'listener_write_req': {'name': 'listener_write_req', 'type': 'gauge'},
    'listener_write_req_max': {'name': 'listener_write_req_max', 'type': 'gauge'},
    'listener_write_res': {'name': 'listener_write_res', 'type': 'gauge'},
    'listener_write_res_max': {'name': 'listener_write_res_max', 'type': 'gauge'},
    'listener_write_started_res': {'name': 'listener_write_started_res', 'type': 'gauge'},
    'listener_write_started_res_max': {'name': 'listener_write_started_res_max', 'type': 'gauge'},
}

REDIS_BIGSTORE = {
    'node_bigstore_free': {'name': 'node_bigstore_free', 'type': 'gauge'},
    'node_bigstore_iops': {'name': 'node_bigstore_iops', 'type': 'gauge'},
    'node_bigstore_kv_ops': {'name': 'node_bigstore_kv_ops', 'type': 'gauge'},
    'node_bigstore_throughput': {'name': 'node_bigstore_throughput', 'type': 'gauge'},
}

REDIS_FLASH = {
    'node_available_flash': 'node_available_flash',
    'node_available_flash_no_overbooking': 'node_available_flash_no_overbooking',
    'node_provisional_flash': 'node_provisional_flash',
    'node_provisional_flash_no_overbooking': 'node_provisional_flash_no_overbooking',
}

DEFAULT_METRICS = [
    REDIS_CLUSTER,
    REDIS_DATABASE,
    REDIS_NODE,
    REDIS_SHARD,
]


ADDITIONAL_METRICS = {
    'RDSE.REPLICATION': REDIS_REPLICATION,
    'RDSE.SHARDREPL': REDIS_SHARD_REPLICATION,
    'RDSE.LISTENER': REDIS_LISTENER,
    'RDSE.PROXY': REDIS_PROXY,
    'RDSE.BIGSTORE': REDIS_BIGSTORE,
    'RDSE.FLASH': REDIS_FLASH,
}
