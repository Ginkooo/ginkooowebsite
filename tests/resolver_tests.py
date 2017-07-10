from unittest import TestCase
import src.resolver as resolver
from config import settings


class ResolverTests(TestCase):

    def check_can_get_parts_of_url(self):
        urls = [
            '/',
            '/foo',
            '/foo/',
            '/foo/bar',
            '/foo/bar/',
            '/foo/bar/car/lar/',
            '/foo/bar/car/lar/dar/',
            '/foo/bar/car/?foo=bar&mar=far',
            '/foo/bar?foo=bar&mar=far/',
            ]

        fn = resolver.get_parts_of_url

        results = []

        for url in urls:
            results.append(fn(url))

        controller, action, params, qs_params = results[0]
        self.assertEqual(settings.DEFAULT_CONTROLLER, controller)
        self.assertEqual(settings.DEFAULT_ACTION, action)
        self.assertFalse(params)
        self.assertFalse(qs_params)

        controller, action, params, qs_params = results[1]
        self.assertEqual('foo', controller)
        self.assertEqual(settings.DEFAULT_ACTION, action)
        self.assertFalse(params)
        self.assertFalse(qs_params)

        controller, action, params, qs_params = results[2]
        self.assertEqual('foo', controller)
        self.assertEqual(settings.DEFAULT_ACTION, action)
        self.assertFalse(params)
        self.assertFalse(qs_params)

        controller, action, params, qs_params = results[3]
        self.assertEqual('foo', controller)
        self.assertEqual('bar', action)
        self.assertFalse(params)
        self.assertFalse(qs_params)

        controller, action, params, qs_params = results[4]
        self.assertEqual('foo', controller)
        self.assertEqual('bar', action)
        self.assertFalse(params)
        self.assertFalse(qs_params)

        controller, action, params, qs_params = results[5]
        self.assertEqual('foo', controller)
        self.assertEqual('bar', action)
        self.assertTrue('car' == params[0])
        self.assertTrue('lar' == params[1])
        self.assertFalse(qs_params)

        controller, action, params, qs_params = results[6]
        self.assertEqual('foo', controller)
        self.assertEqual('bar', action)
        self.assertTrue('car' == params[0])
        self.assertTrue('lar' == params[1])
        self.assertTrue('dar' == params[2])
        self.assertFalse(qs_params)

        controller, action, params, qs_params = results[7]
        self.assertEqual('foo', controller)
        self.assertEqual('bar', action)
        self.assertEqual('car', params[0])
        self.assertEqual(1, len(params))
        self.assertEqual('far', qs_params['mar'])

        controller, action, params, qs_params = results[7]
        self.assertEqual('foo', controller)
        self.assertEqual('bar', action)
        self.assertEqual('car', params[0])
        self.assertEqual(1, len(params))
        self.assertEqual('far', qs_params['mar'])
