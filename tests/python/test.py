#!/usr/bin/env python3

#
#	MetaCall Distributable by Parra Studios
#	Distributable infrastructure for MetaCall.
#
#	Copyright (C) 2016 - 2020 Vicente Eduardo Ferrer Garcia <vic798@gmail.com>
#
#	Licensed under the Apache License, Version 2.0 (the "License");
#	you may not use this file except in compliance with the License.
#	You may obtain a copy of the License at
#
#		http://www.apache.org/licenses/LICENSE-2.0
#
#	Unless required by applicable law or agreed to in writing, software
#	distributed under the License is distributed on an "AS IS" BASIS,
#	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#	See the License for the specific language governing permissions and
#	limitations under the License.
#

from metacall import metacall_load_from_file, metacall

result = metacall_load_from_file('node', ['utils.js'])

if result:
    print('JavaScript file loaded successfully.')

    sum_result = metacall('add', 3, 4)
    print(f'Sum: {sum_result}')

    greeting = metacall('greet', 'World')
    print(greeting)
else:
    print('Failed to load JavaScript file.')
