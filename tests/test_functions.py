import pytest
from main import parse_line,sort_by_area,sort_by_population
def test_parse_line():
    coutry,area,population = parse_line('1 Romania 238397 92046')
    assert area == '238397'

@pytest.mark.parametrize('line, result', [('1 Romania 238397 92046',('Romania','238397','92046')),
                                          ('2 Ukraine 603628 44600000',('Ukraine','603628','44600000')),
                                          ('3 Poland 312679 38433600',('Poland','312679','38433600')),
                                          ('4 Japan 377972 126476461',('Japan','377972','126476461')),
                                          ('5 Germany 357588 83130000',('Germany','357588','83130000')),
                                          ])
def test_parse_line(line,result):
    assert parse_line(line) == result

def test_sort_by_area(prepare_text_file):
    expected = [('Germany','357588','83130000'),
                ('Poland' ,'312679' ,'38433600'),
                ('Romania','238397','92046'),
                ('Denmark','43094','5792202')]
    result = sort_by_area(prepare_text_file)
    assert expected == result

def test_sort_by_population(prepare_text_file):
    expected = [('Germany','357588','83130000'),
                ('Poland' ,'312679' ,'38433600'),
                ('Denmark','43094','5792202'),
                ('Romania','238397','92046')
                ]
    result = sort_by_population(prepare_text_file)
    assert expected == result
