Module smp.cli
==============

Functions
---------

    
`cao(group: <function group at 0x7fe3a796f5b0>, cmd: str) ‑> List[Callable[[Callable[[Any], Any]], Callable[[Any], Any]]]`
:   Retruns wrappers for a click command evaluated from the given arguments.
    
    Args:
        group (click.group): Command group of the command to be under.
        cmd (str): Name of the command.
    
    Returns:
        List[Callable[[Callable[[Any], Any]], Callable[[Any], Any]]]: The wrappers.

    
`command(group: <function group at 0x7fe3a796f5b0>) ‑> Callable[[Callable[[Any], Any]], Callable[[Any], Any]]`
:   Wrapper for click commands.
    
    Args:
        group (click.group): Command group of the command to be under.
    
    Returns:
        Callable[[Callable[[Any], Any]], Callable[[Any], Any]]

    
`fn_log(lvl: int)`
: