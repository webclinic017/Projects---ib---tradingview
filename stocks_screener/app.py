from flask import Flask, render_template, request
import adding_preselected_patterns_from_talib, check_for_setups, data_collection_daily, last_day_data, patterns, test, \
    filter_setups

app = Flask(__name__)


@app.route('/')
def index():
    # pattern = request.args.get('pattern', None)

    return render_template('index.html', patterns=patterns)


@app.route('/collect_data')
def snapshot():
    collected = data_collection_daily.data_collection_daily()
    print('data collected')
    return collected


@app.route('/enrich_data')
def enrich_data():
    adding_preselected_patterns_from_talib.adding_preselected_patterns_to_df_from_ta_lib()

    return 'data enriched'


@app.route('/last_day_data')
def last_day():
    last_day_data.last_day_data()

    return 'last day data filtered'


@app.route('/check_for_setups')
def check():
    check_for_setups.check_for_setups_in_last_days()

    return 'check for setups has been done'


@app.route('/test')
def test1():
    test.test_code()

    return 'test code'


@app.route('/filter')
def filter_setups1():
    filter_setups.filter_setups_for_summary()

    return 'filtered setups'
