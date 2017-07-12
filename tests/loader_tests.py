from src import loader


# TODO: that test
class LoaderTests:

    def check_can_replace_occurences(self):
        test_data = b'Ala ma { zwierze } a kot ma Ale ale Ala tapla sie w ' +\
                    b'{ roztwor }'
        result = loader.replace_occurences(test_data, {'zwierze': 'kota',
                                                       'roztwor': 'kale'})

        self.assertEqual(result,
                         b'Ale ma kota a kot ma Ale ale Ala taple sie w kale')
