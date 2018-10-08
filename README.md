# guess_the_number_py

we need the following packages 
- nixio Python bindings for NIX - https://github.com/G-Node/nixpy documentation and stable version  - https://pypi.org/project/nixio/1.5.0b1/ - 
- odml https://github.com/G-Node/python-odml - open metadata Markup Language - file based format (XML, JSON, YAML) for storing metadata
- NIXódML converter - https://github.com/G-Node/nix-odML-converter - reads in odML / NIX files and writes the metadata structure to newly created NIX / odML file

download all and install with command "python setup.py install"

update metadata to newest version  with https://github.com/G-Node/python-odml/tree/master/odml/scripts/odml_to_rdf 

create metadata nix from xml metadata with nix-odml (convert_odml_to_nix)  

add data to created nix file with convert_bv_to_nix

TODO fix brain vision loader / parser
