project_name/  #at top we have directory with project name,that directory is not a packAGE
# but it containsa both your package and supporting files like setup.py
    README.rst #readme give a quick overview of whats ur project is for and how to use it and
    #it also should help the reader to know if the projet is right for them
    #rst indicates that file written in restructured text
    docs/    #docs is the first subdirectory in project#easy to find/ helps users to find documentation in project
    #most of the projects have some amount of documentaion that belongs to here(docs)
    src/# it contains the actual package directory will have same name as top level directory
    #src contains all the production code including any sub packages
# it also helps us to what version of code we are using
      package_name/
        __init__.py
        more_sorce.py
        sub package1/
           __init__.py
    tests/ #test directory contains all tests for project
    #k33p ur tests outside of package for no.of reasons 1. test & production code serves different purposes
    #2. no need to install tests along with ur packages
    test_code.py

