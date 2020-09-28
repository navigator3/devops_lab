import os
import zipfile
import shutil
import tempfile
import argparse
import logging


path = os.path.join(os.getcwd())
logging.basicConfig(format=u'%(filename)s # %(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.DEBUG, filename='log.txt')
parser = argparse.ArgumentParser()
parser.add_argument("-n", help="Enter zip arhive name", default="test.zip", dest="n")
args = parser.parse_args()
with tempfile.TemporaryDirectory() as tmpdir:
    logging.debug(u'создана временная папка: "%s"' % tmpdir)
    try:
        with zipfile.ZipFile('%s' % args.n, 'r') as zf:
            zf.extractall(path='%s' % tmpdir)
        for i in os.walk(tmpdir):
            if "__init__.py" not in i[2] and i[1] == []:
                logging.warning(u'удалена папка: "%s"' % i[0])
                shutil.rmtree(i[0])
        old_name = (args.n).split(".")[0]
        shutil.make_archive("%s_new" % old_name, 'zip', tmpdir)
        logging.info(u'создан архив: "%s\\%s_new.zip"' % (path, old_name))
        logging.debug(u'удалена временная папка: "%s"' % tmpdir)
    except FileNotFoundError:
        logging.error(u'архив ("%s") не существует' % args.n)
