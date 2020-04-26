![GaifaaYeepun](https://user-images.githubusercontent.com/42882840/80269234-b4ad1c80-86e8-11ea-8a02-567b854170d5.png)

### [日本語](../../README.md) | English

## Overview
GaifaaYeepun is a dictionary website project for Japanese, Thai, and English words/sentences, powered by Django.
This project is designed for Thai people who are learning Japanese, and also Japanese people who are learning Thai.

## Prerequisites
### Server

* Web Server(Windows Server+IIS)(for Production Environment)
* Python(3.6.7 recommended)
* Git

### Client

* PC / Smartphone


## Install
- Production Environment (**To Be Determined**)
- [Development Environment](./install_develop.md)


## Usage (for system users)
On the "Search Page", you can search for words/sentences.
On the "Request Page", you can send a request for the new words/sentences to the system manager .

The details of each page are as follows.
- [Search Page](./howtouse_search.md)

<img src ="https://user-images.githubusercontent.com/42882840/80295910-d8886500-87b1-11ea-8411-2e3267855189.gif" alt="demo" width="400">

- [Request Page](./howtouse_request.md)


## Maintenance
- Update system
  - Get the newest files from this repository, and restart the web server.
- [Add or edit words/sentences](./maintenance_dataedit.md)
- [When receive a request mail from user](./maintenance_reqreceived.md)


## System Configuration
- System Configuration Diagram

![System Configuration Diagram](https://docs.google.com/drawings/d/e/2PACX-1vSLFh_yZhKKi0L7hnfksXXx2Rjc6bimx0RjocQRpwrI5KxMZSzmARUx9lNiZXjq-8R6oSboAkMqkxgV/pub?w=646&h=480)

- [Database Structure](./database.md)
