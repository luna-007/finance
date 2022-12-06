pragma solidity >=0.6.0;

contract SimpleStorage {

    //intialized favouritenumber with a null value
    uint256 public favouriteNumber;
    bool faviouratebool = true;
    string favouritestring = 'string';
    int256 favouriteint = -5;
    address favouriteadress = 0xecf1B917901726fD182A39853fA26222179896AA;
    bytes32 favouritebyte = 'cat';

    struct People {

        string name;     
        uint256 numbers;
    }

    People[] public people;

    function addPerson(string memory _name, uint256 _favouritenumber) public {
        people.push(People(_name, _favouritenumber));
    }

    // people public person = people({numbers:2, name: 'Kila'});

    //creating a function to assign a new value to faviouratenumber
    function store(uint256 _faviourateNumber) public {

        favouriteNumber = _faviourateNumber;
    }

    //pure functions are purely for doing some kind of math
    function retrieve2(uint256 favouritenumber) public pure{
        favouritenumber + favouritenumber;
    }

    //view functions can only return or view the values and not make any changes
    function retrieve() public view returns(uint256) {

        return favouriteNumber;
    }

}