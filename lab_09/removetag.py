# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    removetag.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kawaii <kawaii@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/09/11 09:01:52 by kawaii            #+#    #+#              #
#    Updated: 2024/09/11 09:38:07 by kawaii           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""is HTML a programing language??"""

import re
print(re.sub(r"<?(.[^<>]*)>", " ", input()).split())