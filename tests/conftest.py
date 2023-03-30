import os
import pytest
@pytest.fixture(autouse=True)
def prepare_text_file(tmp_path):
    target_file = os.path.join(tmp_path, 'population.txt')
    with open(target_file, 'w') as file:
        lines = ['1 Denmark 43094 5792202\n',
                 '2 Romania 238397 92046\n',
                 '3 Poland 312679 38433600\n',
                 '4 Germany 357588 83130000\n'
                 ]
        file.writelines(lines)
    return target_file