(function() {
    var oldLog = console.log;
    var oldWarn = console.warn;
    var oldError = console.error;

    console.log = function(...args) {
        if (args.length > 0) {
            oldLog.apply(console, ["lol noob"]);
        }
        return oldLog.apply(console, args);
    };

    console.warn = function(...args) {
        if (args.length > 0) {
            oldWarn.apply(console, ["lol noob"]);
        }
        return oldWarn.apply(console, args);
    };

    console.error = function(...args) {
        if (args.length > 0) {
            oldError.apply(console, ["lol noob"]);
        }
        return oldError.apply(console, args);
    };
})();
