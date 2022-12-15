#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtWidgets import QApplication, QGridLayout
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QTableWidget, QLineEdit, QWidget
from PyQt5.QtNetwork import QNetworkAccessManager
from PyQt5.QtWidgets import QHeaderView


class UrlInput(QLineEdit):
    def __init__(self, browser):
        super(UrlInput, self).__init__()
        self.browser = browser
        # add event listener on "enter" pressed
        self.returnPressed.connect(self._return_pressed)

    def _return_pressed(self):
        url = QUrl(self.text())
        # load url into browser frame
        browser.load(url)


class RequestsTable(QTableWidget):
    header = ["url", "status", "content-type"]

    def __init__(self):
        super(RequestsTable, self).__init__()
        self.setColumnCount(3)
        self.setHorizontalHeaderLabels(self.header)
        header = self.horizontalHeader()
        header.setStretchLastSection(True)
        header.setSectionResizeMode(QHeaderView.ResizeToContents)

    def update(self, data):
        last_row = self.rowCount()
        next_row = last_row + 1
        self.setRowCount(next_row)
        for col, dat in enumerate(data, 0):
            if not dat:
                continue
            self.setItem(last_row, col, QTableWidgetItem(dat))


class Manager(QNetworkAccessManager):
    def __init__(self, table):
        QNetworkAccessManager.__init__(self)
        # add event listener on "load finished" event
        self.finished.connect(self._finished)
        self.table = table

    def _finished(self, reply):
        """Update table with headers, status code and url.
        """
        headers = reply.rawHeaderPairs()
        headers = {str(k): str(v) for k, v in headers}
        content_type = headers.get("Content-Type")
        url = reply.url().toString()
        # getting status is bit of a pain
        status = reply.attribute(QNetworkRequest.HttpStatusCodeAttribute)
        status, ok = status.toInt()
        self.table.update([url, str(status), content_type])


class JavaScriptEvaluator(QLineEdit):
    def __init__(self, page):
        super(JavaScriptEvaluator, self).__init__()
        self.page = page
        self.returnPressed.connect(self._return_pressed)

    def _return_pressed(self):
        frame = self.page.currentFrame()
        result = frame.evaluateJavaScript(self.text())


class ActionInputBox(QLineEdit):
    def __init__(self, page):
        super(ActionInputBox, self).__init__()
        self.page = page
        self.returnPressed.connect(self._return_pressed)

    def _return_pressed(self):
        frame = self.page.currentFrame()
        action_string = str(self.text()).lower()
        if action_string == "b":
            self.page.triggerAction(QWebPage.Back)
        elif action_string == "f":
            self.page.triggerAction(QWebPage.Forward)
        elif action_string == "s":
            self.page.triggerAction(QWebPage.Stop)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # create grid layout
    grid = QGridLayout()
    browser = QWebEngineView()
    url_input = UrlInput(browser)
    requests_table = RequestsTable()

    manager = Manager(requests_table)
    # to tell browser to use network access manager
    # you need to create instance of QWebPage
    page = QWebEnginePage()
    # page.setNetworkAccessManager(manager)
    js_eval = JavaScriptEvaluator(page)
    act_input = ActionInputBox(page)
    browser.setPage(page)

    # url_input at row 1 column 0 of our grid
    grid.addWidget(url_input, 1, 0)
    # browser frame at row 2 column 0 of our grid
    grid.addWidget(browser, 2, 0)
    grid.addWidget(requests_table, 3, 0)
    grid.addWidget(js_eval, 4, 0)
    grid.addWidget(js_eval, 5, 0)
    # main app window
    main_frame = QWidget()
    main_frame.setLayout(grid)
    main_frame.show()

    # close app when user closes window
    sys.exit(app.exec_())
