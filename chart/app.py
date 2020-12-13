from flask import Flask, Markup, render_template
import pandas

colnames = ['chn_name', 'metric_value']
data = pandas.read_csv('test.csv', names=colnames)

metric_value = data.metric_value.tolist()
chn_name = data.chn_name.tolist()

metric_value.pop(0)
chn_name.pop(0)

app = Flask(__name__)

labels = chn_name 

values = metric_value

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

@app.route('/bar')
def bar():
    bar_labels=labels
    bar_values=values
    return render_template('bar_chart.html', title='HVR METRICS : ', max=62712, labels=bar_labels, values=bar_values)

@app.route('/line')
def line():
    line_labels=labels
    line_values=values
    return render_template('line_chart.html', title='HVR METRICS : ', max=62712, labels=line_labels, values=line_values)

@app.route('/pie')
def pie():
    pie_labels = labels
    pie_values = values
    return render_template('pie_chart.html', title='HVR METRICS : ', max=62712, set=zip(values, labels, colors))

if __name__ == '__main__':
    app.debug = True

