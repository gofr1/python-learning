
    <?xml version="1.0" ?> // is a tree
    <metric> // root element
        <time>2021-02-19T20:23:30.804564</time> // elements or nodes have tags with data
        <name></name>
        <value></value>
        <labels>
            <label key="host" value="prod"/> // key and value are properties
            <label key="version" value="1.2.6"/> // label is child element/node of labels
        </labels>
    </metric>

There are two ways to work with XML:

* DOM (Document Object Module) (Everything is in memory)
* SAX (Simple API for XML) (Iterative and good for large XML documents)
