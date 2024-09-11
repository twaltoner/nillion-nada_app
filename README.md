## MaxGame
### Game built on Nada where 3 players give number nad max one wins, but programm everytime generates number from 0 to 10000 which is max, so if your number is more, you're out, so you cant just give huge num and win

## How to test it
Clone the repo or fork and clone your repo
```
git clone https://github.com/twaltoner/nillion-nada_app
```
If you're here I assume you know how  to work with nada. If not, see how to start [HERE](https://docs.nillion.com/nada-by-example)

Use nada to build app
```
nada build
```
And run it with values from tests
```
nada run game_test
```
Output should be tie or win of any of 3 players, you can also build your own tests and test with it ( check ```tests/game_test.yaml``` for example)
