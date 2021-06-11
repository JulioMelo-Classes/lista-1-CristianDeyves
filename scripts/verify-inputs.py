#!/usr/bin/env python3

from subprocess import run, PIPE
# This provides functions for interacting with the operating system 
#  from os import path
# This provides access to stdin/stdout/stderr as well as command line arguments.
import sys
import glob
import os

# We are expecting at least one argument
if len(sys.argv) == 1:
    sys.exit(-1)

# This is the name of the executable we want to test.
executable = sys.argv[1]

# Use this to count how many input test file we've got.
def count_files(path,extension):
  list_dir = []
  list_dir = os.listdir(path)
  count = 0
  for file in list_dir:
    if file.endswith(extension): # eg: '.txt'
      count += 1
  return count

# Define the location where we read the input and the expected answers.
root_dir = os.path.realpath('..')
input_dir = root_dir + '/data_in'
expected_dir = root_dir + '/data_expected'

# This will hold the output of each execution so we can
# compare this to the expected answer stored in data_expected.
#  outputs = []

# Keep track of the possible tests' outcome.
n_tests = 0
n_io_errors = 0
n_runtime_errors = 0
n_failures = 0
how_many_tests = count_files( input_dir, 'txt')
# To improve readibility we padd test number with zeros.
zero_padding = len( str(how_many_tests) ) + 1

print('\n\033[1;36m>>> RODANDO TESTES DE COMPARAÇÃO DE ENTRADA/SAÍDA ESPERADAS <<< \033[0;0m\n')

# Let us run the program with every input defined for this test.
for file in glob.glob( input_dir + '/*.txt' ):

    # [1]-- PREPARATION
    n_tests +=1
    # Retrieve the file name, exclusing the path.
    basename = os.path.basename(file) # as in: file.ext
    # os.path.splitext() method in Python is used to split the path name into a pair root and ext. 
    # Here, ext stands for extension and has the extension portion of the specified path while 
    # root is everything except ext part.
    # root is stored in [0] and ext in [1].
    file_name = os.path.splitext(basename)[0] # Just the file name, no extension.
    ext_name = os.path.splitext(basename)[1]
    # Compose the test name based on the input file and test count.
    test_name = 'test ' + str(n_tests).zfill(zero_padding) + ': ' +  file_name

    # This is the relative path to the corresponding file name with the expected output.
    expected_filename = expected_dir + '/' + file_name + '_OUT' + ext_name

    # Let us check whether the correct (reference) output file does exist.
    if not os.path.exists(expected_filename):
        print("\033[1;33m[%s]: Gabarito não encontrado para o arquivo '%s'. Ignorando...\033[0;0m" % (test_name, basename))
        n_failures +=1
        continue # Go to the next test case.

    # [2]-- READ THE INPUT FILE CONTENT
    with open(file) as f:
        input = f.read()

    # [3]-- RUN THE PROGRAM ON THE CURRENT INPUT FILE
    # args       – returns the actual commands executed
    # returncode – returns the return code of the output; 0 means no error
    # stdout     – captured stdout from the child process
    # stderr     – captured stderr stream from the child process
    result = run([executable], capture_output=True, text=True, input=input)

    # Check the process' return code 
    if result.returncode != 0:
        print('\033[1;31m[%s]: Erro na execução do programa.\033[0;0m' % test_name )
        print("\033[1;31m> Saída (stdout):\n=------[ início ]------=\n%s.\n=------[ fim ]---------=\n\033[0;0m" % (result.stdout))
        print("\033[1;31m> Erro (stderr):\n=------[ início ]------=\n%s.\n=------[ fim ]---------=\n\033[0;0m" % (result.stderr))
        n_runtime_errors +=1
        continue # Go to the next test case.

    # [4]-- GET THE ACTUAL OUTPUT WITH THE EXPECTED OUTPUT
    # Get the output generated by the execution, from the standard output.
    actual_output = result.stdout.strip()

    # [5]-- GET THE EXPECTED OUTPUT FILE CONTENT
    # Get the expected output content (the expected result).
    with open(expected_filename) as g:
        expected_output = g.read().strip()

    # [6]-- COMPARE THE ACTUAL x EXPECTED OUTPUTS
    if actual_output == expected_output:
        print("\033[0;32m[%s]: OK\033[0;0m" % test_name)
    else:
        n_io_errors +=1
        print("\033[1;31m[%s]: Erro. \033[0;0m" % (test_name))
        print("\033[1;31m> Esperado:\n=------[ início ]------=\n%s\n=------[ fim ]---------=\n\033[0;0m" % (expected_output))
        print("\033[1;31m> Retornado:\n=------[ início ]------=\n%s\n=------[ fim ]---------=\n\033[0;0m" % (actual_output))
# End of 'for' loop.

# -----------------------------------------------------------------------------
# FINAL TEST SUMMARY
# -----------------------------------------------------------------------------
n_success = n_tests - ( n_failures + n_io_errors + n_runtime_errors )

print("\033[1;32m\nSumário dos testes:\033[0;0m")
print("\033[1;32m• Falhas........: %s\033[0;0m" % n_failures )
print("\033[1;32m• Erros E/S.....: %s\033[0;0m" % n_io_errors )
print("\033[1;32m• Erros Execução: %s\033[0;0m" % n_runtime_errors )
print("\033[1;32m• Sucessos......: %s\033[0;0m" % n_success )

# Display the appropriate message
if ( n_io_errors != 0 or n_runtime_errors != 0):
    print('\033[5;31;47m   >>> ATENÇÃO: Erros foram encontrados no teste! Confira o LOG acima. <<<   \033[0;0m\n')
if ( n_failures != 0 ):
    print('\033[5;34;47m   >>> ATENÇÃO: Alguns testes falharam por falta de gabarito. Confira o LOG acima. <<<   \033[0;0m\n')
if ( n_tests == n_success ): # Total of tests OK
    print('\n\033[1;32m>>> TESTE CONCLUÍDO COM SUCESSO! <<< \033[0;0m')
