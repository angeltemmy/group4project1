{% set config = {
    "extract_type": "incremental",
    "incremental_column": '"properties.time"',
    "source_table_name": "table_earthquake_1_data"
} %}
select
*
from
    {{ config["source_table_name"] }} 

{% if is_incremental %}
    where {{ config["incremental_column"] }} > '{{ incremental_value }}'
{% endif %}
