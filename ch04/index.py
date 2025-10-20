from flask import Flask, request, render_template, jsonify
import random
import RPi.GPIO as GPIO
import time

app = Flask(__name__)
