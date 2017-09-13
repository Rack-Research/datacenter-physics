#! /usr/bin/python

"""
This is the base script for Rack Research - Datacenter Physics

This Framework is developed with Python 2.7.5
"""

import os
import sys
import psutil
import platform
import commands
import socket
import multiprocessing
import threading
import time
import logging
import json
import itertools
import csv


"""
This script will intend to get

System Hardware information

System OS information

System Application information

System Network information

System Logging information


All such details will be taken and an object will be created. The data will be dumped every minute.

IT HAS TO BE ENSURED THAT WE ARE AS LIGHT AS POSSIBLE MONITORING OUR OWN PROCESS AND CPU & MEMORY CONSUMPTION

All these will be stored in a SQL and No-SQL DBS

List of supported DBs are

SQL: MySQL, MariaDB, MemSQL, MSSQL, IBMDB2, Oracle DB, PostgreSQL, SQlite


NOSQL: Document Store DB ( Couchbase / MongoDB )  | Wide Column Store ( Cassandra / BigTable / HBase / Amazon DynamoDB )

"""


print "Running script rr_dc_base.py"