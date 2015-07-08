var dmr;
if(typeof(dmr) == 'undefined') {
    dmr = {};
}

if(typeof(dmr.index) == 'undefined') {
    dmr.index = {};
}

dmr.index.boot = function() {
    function plot_activity(series_config, minimum_time, maximum_time) {
        $('#activity_chart').highcharts({
            chart: {
                type: 'spline',
                zoomType: 'x'
            },
            title: {
                text: 'DNS Activity'
            },
            xAxis: {
                type: 'datetime',
                labels: {
                    format: '{value:(%m-%d) %H}',
                    rotation: -45,
                    style: {
                        fontSize: '13px',
                        fontFamily: 'Verdana, sans-serif'
                    }
                },
                min: minimum_time,
                max: maximum_time,
                minTickInterval: 60 * 60 * 1000
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
        var series_config = [], minimum_time = null, maximum_time = null;

        // Bin the data.

        for(var type in data) {
            var rows, distilled = [];

            rows = data[type];

            for(var i in rows) {
                var row, timestamp_tuple, timestamp, type, count;

                row = rows[i];

                timestamp_tuple = row[0];
                count = row[1];

                timestamp = new Date(
                    timestamp_tuple[0], 
                    timestamp_tuple[1] - 1, 
                    timestamp_tuple[2], 
                    timestamp_tuple[3]);

                distilled[distilled.length] = [timestamp.getTime(), count];

                if(minimum_time != null) {
                    minimum_time = Math.min(minimum_time, timestamp);
                } else {
                    minimum_time = timestamp;
                }

                if(maximum_time != null) {
                    maximum_time = Math.max(maximum_time, timestamp);
                } else {
                    maximum_time = timestamp;
                }
            }

            series_config[series_config.length] = {
                name: type.toUpperCase(),
                data: distilled,
                pointInterval: 60 * 60 * 1000
            };
        }

        plot_activity(series_config, minimum_time, maximum_time);
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
