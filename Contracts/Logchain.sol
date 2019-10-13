pragma solidity ^0.5.0;

contract TodoList {
    uint public logCount = 0;
    struct Log {
        uint log_id;
        uint server_id;
        string typ;
        string data;
        string timestamp;
    }

    // Storing data in-memory on blockchain
    // Reader function will be provided by solidity
    mapping(uint => Log) public logs;

    event LogCreated(
        uint log_id,
        uint server_id,
        string typ,
        string data,
        string timestamp
    );

    // constructor() public {
    //     createLog(-1,);
    // }

    function createLog(uint server_id,string memory typ,string memory data,string memory timestamp) public {
        logCount++;
        logs[logCount] = Log(logCount,server_id,typ,data,timestamp);
        // Broadcast an event to alert everyone that an event has occured
        emit LogCreated(logCount,server_id,typ,data,timestamp);

    }

}