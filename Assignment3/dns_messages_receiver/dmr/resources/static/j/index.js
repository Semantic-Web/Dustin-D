var dmr;
if(typeof(dmr) == 'undefined') {
    dmr = {};
}

if(typeof(dmr.index) == 'undefined') {
    dmr.index = {};
}

dmr.index.boot = function() {
    function plot_activity(series_config) {
        $('#activity_chart').highcharts({
            chart: {
                zoomType: 'x'
            },
            title: {
                text: 'DNS Activity'
            },
            xAxis: {
                type: 'datetime',
                labels: {
                    rotation: -45,
                    style: {
                        fontSize: '13px',
                        fontFamily: 'Verdana, sans-serif'
                    }
                }
            },
            yAxis: {
                min: 0,
                title: {
                    text: 'Count'
                }
            },
            series: series_config
        });
    }

    function activity_success(data) {
        var series_data, series_config;

        series_data = {};

        // Bin the data.

        for(var i in data.rows) {
            var row, timestamp_tuple, timestamp, type, count;

            row = data.rows[i];

            timestamp_tuple = row[0];
            type = row[1];
            count = row[2];

            timestamp = Date.UTC(
                timestamp_tuple[0], 
                timestamp_tuple[1] - 1, 
                timestamp_tuple[2], 
                timestamp_tuple[3]);

            if(typeof(series_data[type]) == 'undefined') {
                series_data[type] = [[timestamp, count]];
            } else {
                series_data[type][series_data[type].length] = [timestamp, count];
            }
        }

        // Now, define the config.

        series_config = [];

        for(var type in series_data) {
            var data = series_data[type];

            series_config[series_config.length] = {
                type: 'area',
                name: type.toUpperCase(),
                data: data
            };
        }

        plot_activity(series_config);
    }

    function activity_error() {
        alert("There was a problem.");
    }

    $.ajax({
        url: '/dns/ajax/activity/hour',
        method: 'get',
        dataType: 'json',
        success: activity_success,
        error: activity_error
    });
}

$(dmr.index.boot);
