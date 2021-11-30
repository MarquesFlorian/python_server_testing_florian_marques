import pytest
import requests
import time

def test_status_code_200():
    """
    a test that calls the website's url and confirms a code reply of 200. The site output is correct: 
    """
    url = 'http://127.0.0.1:5000/means?int=1&int=2&int=7'

    resp = requests.get(url)
    assert resp.status_code == 200

def test_mean_of_list_is_correct():
    """
    a test that sends a GET request to the website and confirms that the website returns the correct answer.
    """
    url = 'http://127.0.0.1:5000/means?int=1&int=2&int=7'
    
    resp = requests.get(url)
    assert resp.content == b'Mean of the list is : 3.3333333333333335'

def test_stress_requests():
    """
    The site can handle stress: the average response time of the site should be below 100 ms per request, when 1000 requests are sent per second.
    """
    url = 'http://127.0.0.1:5000/means?int=1&int=2&int=7'
    
    started_time = time.time()
    
    for i in range(1000):
        requests.get(url)
    
    end_time = time.time()-started_time
    
    assert (end_time/1000) < 100

