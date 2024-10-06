{% set config = {
    "extract_type": "full",
    "source_table_name": "table_earthquake_1_data"
} %}
select
*
from
    {{ config["source_table_name"] }}
