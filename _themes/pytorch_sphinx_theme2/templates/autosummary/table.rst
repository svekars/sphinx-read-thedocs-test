{% extends "!autosummary/table.rst" %}

{% block table %}
THIS IS A CUSTOM TEMPLATE TEST
.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Name
     - Description
   {% for item in items %}
   * - {{ item }}
     - {{ item | truncate(60) }}
   {% endfor %}
{% endblock %}
