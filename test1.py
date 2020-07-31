#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests


def send_message(title, content):
    url = 'https://sc.ftqq.com/SCU107671T85e61a41dce29ee18a8b43b32f30d3745f222e3e7abf0.send'
    r = requests.post(url, params={'text': title, 'desp': content})
    print(r.text)


if __name__ == '__main__':
    send_message('1', '2')

