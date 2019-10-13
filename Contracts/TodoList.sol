pragma solidity ^0.5.0;

contract TodoList {
    uint public taskCount = 0;
    struct Task {
        uint id;
        string content;
        bool completed;
    }

    // Storing data in-memory on blockchain
    // Reader function will be provided by solidity
    mapping(uint => Task) public tasks;

    event TaskCreated(
        uint id,
        string content,
        bool completed
    );

    constructor() public {
        createTask("Hello Aman");
    }

    function createTask(string memory _content) public {
        taskCount++;
        tasks[taskCount] = Task(taskCount,_content,false);
        // Broadcast an event to alert everyone that an event has occured
        emit TaskCreated(taskCount,_content, false);

    }

}