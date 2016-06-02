'''
Created on May 27, 2016

@author: root
'''
import unittest
import sys
from oslo.config import cfg
import cloudkitty.collector
from stevedore import driver
from stevedore import extension
from cloudkitty.collector.ceilometer import CeilometerCollector as collector
from __builtin__ import str

#from cloudkitty import tests

FETCHERS_NAMESPACE = 'cloudkitty.tenant.fetchers'
COLLECTORS_NAMESPACE = 'cloudkitty.collector.backends'
FETCHERS_NAMESPACE = 'cloudkitty.tenant.fetchers'
TRANSFORMERS_NAMESPACE = 'cloudkitty.transformers'
PROCESSORS_NAMESPACE = 'cloudkitty.rating.processors'
STORAGES_NAMESPACE = 'cloudkitty.storage.backends'

CONF = cfg.CONF
CONF.import_opt('backend', 'cloudkitty.storage', 'storage')
CONF.import_opt('backend', 'cloudkitty.tenant_fetcher', 'tenant_fetcher')

class Test(unittest.TestCase):

    def setUp(self):
        #start=1464525000,end=1464525060,project_id=982ea1a1fa2f4efda4a89bee11425c75,q_filter=None
        #func = getattr(self, 'get_bandwidth')
        
        self.timestampStart = '1464739200'
        self.timestampEnd = '1467244800' 
        
        
        
        self.transformers = {}
        self._load_transformers()

        self.collector_args = {'transformers': self.transformers,
                          'period': '60'}

        
        self.collector = driver.DriverManager(
            COLLECTORS_NAMESPACE,
            CONF.collect.collector,
            invoke_on_load=True,
            invoke_kwds=self.collector_args).driver
        pass
        
    def tearDown(self):
        pass


    def test_get_bandwidth(self):
        print sys._getframe().f_code.co_name
        check_dt={}
        #raw_data =func( '1464525000', '1464525060', '982ea1a1fa2f4efda4a89bee11425c75', None)
        check_dt= self.collector.retrieve('bandwidth',self.timestampStart,self.timestampEnd)
        
        vol = check_dt['bandwidth'][0]
        print vol
        self.assertIsNotNone(vol,'is none')
        #self.assertEqual(calc_dt, check_dt)

    def test_get_bandwidth_noData(self):
        print sys._getframe().f_code.co_name
        check_dt={}
        #raw_data =func( '1464525000', '1464525060', '982ea1a1fa2f4efda4a89bee11425c75', None)
        try:
            check_dt= self.collector.retrieve('bandwidth','946684800','946771200')
        except Exception as e:
            s = str(e)
            print s
            self.assertGreaterEqual(s.find('no data for resource'), 0)
        
    def test_get_volume(self):
        print sys._getframe().f_code.co_name
        check_dt={}
        #raw_data =func( '1464525000', '1464525060', '982ea1a1fa2f4efda4a89bee11425c75', None)
        check_dt= self.collector.retrieve('volume',self.timestampStart,self.timestampEnd)
        
        vol = check_dt['volume'][0]
        print vol
        self.assertIsNotNone(vol,'is none')
        #self.assertEqual(calc_dt, check_dt)

    def test_get_volume_noData(self):
        print sys._getframe().f_code.co_name
        check_dt={}
        #raw_data =func( '1464525000', '1464525060', '982ea1a1fa2f4efda4a89bee11425c75', None)
        try:
            check_dt= self.collector.retrieve('volume','946684800','946771200')
        except Exception as e:
            s = str(e)
            print s
            self.assertGreaterEqual(s.find('no data for resource'), 0)
            
    def test_get_volume_size(self):
        print sys._getframe().f_code.co_name
        check_dt={}
        #raw_data =func( '1464525000', '1464525060', '982ea1a1fa2f4efda4a89bee11425c75', None)
        check_dt= self.collector.retrieve('volume.size',self.timestampStart,self.timestampEnd)
        
        vol = check_dt['volume.size'][0]
        print vol
        self.assertIsNotNone(vol,'is none')
        #self.assertEqual(calc_dt, check_dt)

    def test_get_volume_size_noData(self):
        print sys._getframe().f_code.co_name
        check_dt={}
        #raw_data =func( '1464525000', '1464525060', '982ea1a1fa2f4efda4a89bee11425c75', None)
        try:
            check_dt= self.collector.retrieve('volume.size','946684800','946771200')
        except Exception as e:
            s = str(e)
            print s
            self.assertGreaterEqual(s.find('no data for resource'), 0)
            
    def test_get_network_bw_lbs_in(self):
        print sys._getframe().f_code.co_name
        check_dt={}
        #raw_data =func( '1464525000', '1464525060', '982ea1a1fa2f4efda4a89bee11425c75', None)
        check_dt= self.collector.retrieve('network.bw.lbs.in',self.timestampStart,self.timestampEnd)
        
        vol = check_dt['network.bw.lbs.in'][0]
        print vol
        self.assertIsNotNone(vol,'is none')
        #self.assertEqual(calc_dt, check_dt)

    def test_get_network_bw_lbs_in_noData(self):
        print sys._getframe().f_code.co_name
        check_dt={}
        #raw_data =func( '1464525000', '1464525060', '982ea1a1fa2f4efda4a89bee11425c75', None)
        try:
            check_dt= self.collector.retrieve('network.bw.lbs.in','946684800','946771200')
        except Exception as e:
            s = str(e)
            print s
            self.assertGreaterEqual(s.find('no data for resource'), 0)
            
    def test_get_network_bw_lbs_out(self):
        print sys._getframe().f_code.co_name
        check_dt={}
        #raw_data =func( '1464525000', '1464525060', '982ea1a1fa2f4efda4a89bee11425c75', None)
        check_dt= self.collector.retrieve('network.bw.lbs.out',self.timestampStart,self.timestampEnd)
        
        vol = check_dt['network.bw.lbs.out'][0]
        print vol
        self.assertIsNotNone(vol,'is none')
        #self.assertEqual(calc_dt, check_dt)

    def test_get_network_bw_lbs_out_noData(self):
        print sys._getframe().f_code.co_name
        check_dt={}
        #raw_data =func( '1464525000', '1464525060', '982ea1a1fa2f4efda4a89bee11425c75', None)
        try:
            check_dt= self.collector.retrieve('network.bw.lbs.out','946684800','946771200')
        except Exception as e:
            s = str(e)
            print s
            self.assertGreaterEqual(s.find('no data for resource'), 0)
            
    def test_get_network_bw_lbs_pool(self):
        print sys._getframe().f_code.co_name
        check_dt={}
        #raw_data =func( '1464525000', '1464525060', '982ea1a1fa2f4efda4a89bee11425c75', None)
        check_dt= self.collector.retrieve('network.bw.lbs.pool',self.timestampStart,self.timestampEnd)
        
        vol = check_dt['network.bw.lbs.pool'][0]
        print vol
        self.assertIsNotNone(vol,'is none')
        #self.assertEqual(calc_dt, check_dt)

    def test_get_network_bw_lbs_pool_noData(self):
        print sys._getframe().f_code.co_name
        check_dt={}
        #raw_data =func( '1464525000', '1464525060', '982ea1a1fa2f4efda4a89bee11425c75', None)
        try:
            check_dt= self.collector.retrieve('network.bw.lbs.pool','946684800','946771200')
        except Exception as e:
            s = str(e)
            print s
            self.assertGreaterEqual(s.find('no data for resource'), 0)
                
    def test_get_snapshot(self):
        print sys._getframe().f_code.co_name
        check_dt={}
        #raw_data =func( '1464525000', '1464525060', '982ea1a1fa2f4efda4a89bee11425c75', None)
        check_dt= self.collector.retrieve('snapshot',self.timestampStart,self.timestampEnd)
        
        vol = check_dt['snapshot'][0]
        print vol
        self.assertIsNotNone(vol,'is none')
        #self.assertEqual(calc_dt, check_dt)

    def test_get_snapshot_noData(self):
        print sys._getframe().f_code.co_name
        check_dt={}
        #raw_data =func( '1464525000', '1464525060', '982ea1a1fa2f4efda4a89bee11425c75', None)
        try:
            check_dt= self.collector.retrieve('snapshot','946684800','946771200')
        except Exception as e:
            s = str(e)
            print s
            self.assertGreaterEqual(s.find('no data for resource'), 0)
                    
    def test_get_snapshot_size(self):
        print sys._getframe().f_code.co_name
        check_dt={}
        #raw_data =func( '1464525000', '1464525060', '982ea1a1fa2f4efda4a89bee11425c75', None)
        check_dt= self.collector.retrieve('snapshot.size',self.timestampStart,self.timestampEnd)
        
        vol = check_dt['snapshot.size'][0]
        print vol
        self.assertIsNotNone(vol,'is none')
        #self.assertEqual(calc_dt, check_dt)

    def test_get_snapshot_size_noData(self):
        print sys._getframe().f_code.co_name
        check_dt={}
        #raw_data =func( '1464525000', '1464525060', '982ea1a1fa2f4efda4a89bee11425c75', None)
        try:
            check_dt= self.collector.retrieve('snapshot.size','946684800','946771200')
        except Exception as e:
            s = str(e)
            print s
            self.assertGreaterEqual(s.find('no data for resource'), 0)

    def test_get_radosgw_api_request(self):
        print sys._getframe().f_code.co_name
        check_dt={}
        #raw_data =func( '1464525000', '1464525060', '982ea1a1fa2f4efda4a89bee11425c75', None)
        check_dt= self.collector.retrieve('radosgw.api.request',self.timestampStart,self.timestampEnd)
        
        vol = check_dt['radosgw.api.request'][0]
        print vol
        self.assertIsNotNone(vol,'is none')
        #self.assertEqual(calc_dt, check_dt)
        
    def test_get_radosgw_api_request_noData(self):
        print sys._getframe().f_code.co_name
        check_dt={}
        #raw_data =func( '1464525000', '1464525060', '982ea1a1fa2f4efda4a89bee11425c75', None)
        try:
            check_dt= self.collector.retrieve('radosgw.api.request','946684800','946771200')
        except Exception as e:
            s = str(e)
            print s
            self.assertGreaterEqual(s.find('no data for resource'), 0)




    def _load_transformers(self):
        self.transformers = {}
        transformers = extension.ExtensionManager(
            TRANSFORMERS_NAMESPACE,
            invoke_on_load=True)

        for transformer in transformers:
            t_name = transformer.name
            t_obj = transformer.obj
            self.transformers[t_name] = t_obj
            
if __name__ == '__main__':
    unittest.main()
    
