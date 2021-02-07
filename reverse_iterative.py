# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

def reverse_iterative(S):
  """Reverse elements in sequence S."""
  start, stop = 0, len(S)
  while start < stop - 1:
    print('reverse:', S)
    S[start], S[stop-1] = S[stop-1], S[start]  # swap first and last
    start, stop = start + 1, stop - 1          # narrow the range

if __name__ == '__main__':
  S = ['0','1','2','3','4','5','6','7','8']
  print(S)
  reverse_iterative(S)
  print(S)