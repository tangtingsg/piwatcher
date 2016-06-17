import config
import utils
import urllib.parse
import urllib.request
import urllib.error
import ast

API_URL = "http://ipiwatcher.applinzi.com/api.php"
KEY_ACTION = 'action'
KEY_TIME = 'time'


def get_identity_para():
    identity = config.get_uuid_psw()
    psw_salt = utils.psw_salt(identity['UUID'], identity['PSW'])
    para = {'uuid': identity['UUID'], 'psw': psw_salt}
    return para


def create_account():
    para = get_identity_para()
    para[KEY_ACTION] = 'create'
    real_url = API_URL + '?' + urllib.parse.urlencode(para)
    return call_web_api(real_url)


def report_motion(motion_time):
    para = get_identity_para()
    para[KEY_ACTION] = 'add'
    para[KEY_TIME] = int(motion_time)
    real_url = API_URL + '?' + urllib.parse.urlencode(para)
    print("report_motion:%s" % real_url)
    return call_web_api(real_url)


def call_web_api(url):
    try:
        resp = urllib.request.urlopen(url)
        data = resp.read().decode('utf-8')
        dct = ast.literal_eval(data)
        return dct['status'] == 'ok'
    except (urllib.error.HTTPError, urllib.error.URLError):
        print("Network Error")
    except (ValueError, SyntaxError):
        print("Response Not Json")
    except:
        print("Other Exception")

    return False
