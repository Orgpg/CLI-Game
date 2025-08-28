from setuptools import setup, find_packages

setup(
    name="cli-games-hnd68",
    version="0.1",
    packages=find_packages(),
    entry_points={
    'console_scripts': [
        'guessing=cli_games.guess_the_number:play_game',
        'mathquiz=cli_games.math_quiz_duel:play_game',
        'typerace=cli_games.typing_speed_race:play_game',
    ],
},

)
