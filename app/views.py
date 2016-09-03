from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'a_turtle'}
    return render_template(
        'index.html',
        title="Home",
        user=user
    )


@app.route('/rants')
def rants():
    user = {'nickname': 'a_turtle'}
    return render_template(
        'rants.html',
        title="Rants",
        user=user
    )


@app.route('/tables')
def tables():
    user = {'nickname': 'a_turtle'}
    return render_template(
        'tables.html',
        title="tables",
        user=user
    )


@app.route('/math')
def math():
    user = {'nickname': 'a_turtle'}
    return render_template(
        'math.html',
        title="math",
        user=user
    )


@app.route('/iframe')
def iframe():
    user = {'nickname': 'a_turtle'}
    return render_template(
        'iframe.html',
        title="iframe",
        user=user
    )


@app.route('/layout01')
def layout01():
    user = {'nickname': 'a_turtle'}
    return render_template(
        'layout01.html',
        title="layout01",
        user=user
    )


@app.route('/class-vs-id')
def class_vs_id():
    user = {'nickname': 'a_turtle'}
    return render_template(
        'class-vs-id.html',
        title="class-vs-id",
        user=user
    )


@app.route('/machine-learning/index')
def machine_learning__index():
    user = {'nickname': 'a_turtle'}
    return render_template(
        'machine-learning/index.html',
        title="machine learning",
        user=user
    )


@app.route('/computer-languages/index')
def computer_languages__index():
    user = {'nickname': 'a_turtle'}
    return render_template(
        'computer-languages/index.html',
        title="computer languages",
        user=user
    )


@app.route('/systems-biology/index')
def systems_biology__index():
    user = {'nickname': 'a_turtle'}
    return render_template(
        'systems-biology/index.html',
        title="systems biology",
        user=user
    )


@app.route('/regex-pnp/regex')
def regex_pnp__regex():
    user = {'nickname': 'a_turtle'}
    return render_template(
        'regex-pnp/regex.html',
        title="Regular expressions",
        user=user
    )


@app.route('/machine-learning/method-web/lda')
def machine_learning__method_web__lda():
    user = {'nickname': 'a_turtle'}
    return render_template(
        'machine-learning/method-web/lda.html',
        title="LDA",
        user=user
    )


@app.route('/machine-learning/method-web/index')
def machine_learning__method_web__index():
    user = {'nickname': 'a_turtle'}
    return render_template(
        'machine-learning/method-web/index.html',
        title="Machine learning",
        user=user
    )


@app.route('/machine-learning/method-web/qda')
def machine_learning__method_web__qda():
    user = {'nickname': 'a_turtle'}
    return render_template(
        'machine-learning/method-web/qda.html',
        title="QDA",
        user=user
    )


@app.route('/machine-learning/method-web/bayes-classifier')
def machine_learning__method_web__bayes_classifier():
    user = {'nickname': 'a_turtle'}
    return render_template(
        'machine-learning/method-web/bayes-classifier.html',
        title="Bayes Classifier",
        user=user
    )


@app.route('/machine-learning/method-web/linear-regression')
def machine_learning__method_web__linear_regression():
    user = {'nickname': 'a_turtle'}
    return render_template(
        'machine-learning/method-web/linear-regression.html',
        title="Linear Regression",
        user=user
    )


@app.route('/machine-learning/method-web/k-means')
def machine_learning__method_web__k_means():
    user = {'nickname': 'a_turtle'}
    return render_template(
        'machine-learning/method-web/k-means.html',
        title="K Means",
        user=user
    )


@app.route('/machine-learning/daily-coverage')
def machine_learning__daily_coverage():
    user = {'nickname': 'a_turtle'}
    return render_template(
        'machine-learning/daily-coverage.html',
        title="Daily Coverage",
        user=user
    )


@app.route('/machine-learning/statistics-background')
def machine_learning__statistics_background():
    user = {'nickname': 'a_turtle'}
    return render_template(
        'machine-learning/statistics-background.html',
        title="Statistics Background",
        user=user
    )


@app.route('/machine-learning/chapter-notes')
def machine_learning__chapter_notes():
    user = {'nickname': 'a_turtle'}
    return render_template(
        'machine-learning/chapter-notes.html',
        title="Chapter Notes",
        user=user
    )


@app.route('/systems-biology/papers')
def systems_biology__papers():
    user = {'nickname': 'a_turtle'}
    return render_template(
        'systems-biology/papers.html',
        title="Papers",
        user=user
    )


@app.route('/html-test/t')
def html_test__t():
    user = {'nickname': 'a_turtle'}
    return render_template(
        'html-test/t.html',
        title="T-Test",
        user=user
    )
