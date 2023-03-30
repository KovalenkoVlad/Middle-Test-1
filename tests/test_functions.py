import pytest
from main import parse_line
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
