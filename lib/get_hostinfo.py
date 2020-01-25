# -*- coding: utf-8 -*-
"""
Get target host's connection info.
"""

from __future__ import (division, print_function, absolute_import,
                        unicode_literals)

import re
import sys

from lib import iplist_searcher as search


def _print_choose_targethost(iplist_infos):
    order = {}
    idx = 0
    for iplist, hostinfo_sheets in iplist_infos.items():
        print('###############################')
        print('iplist: {}\n'.format(iplist))

        for hostinfo in hostinfo_sheets:
            idx += 1
            order[idx] = hostinfo
            print("    {index}:  {host}  {address}".format(
                index=str(idx),
                host=hostinfo.name,
                address=hostinfo.ipaddress))
        print('###############################')

    try:
        input_number = input('Please select target host no. >>>  ')
        input_number = int(input_number)
        if input_number not in order:
            raise KeyError
    except (NameError, KeyError, KeyboardInterrupt, SyntaxError, ValueError):
        print('')
        print('Invalid number was inputed.')
        sys.exit(1)

    target_hostinfo = order[input_number]
    print('Connect to {host} : {ip}.'.format(host=target_hostinfo.name,
                                             ip=target_hostinfo.ipaddress))
    return target_hostinfo


def _sepalate_hitting_host(all_hostinfos, part_of_host):
    """ Get pattern matched hostname's ipaddress from all iplist files. """
    new_iplist_infos = {}
    for iplist, hostinfo_sheets in all_hostinfos.items():
        iplist_hostinfos = []
        for sheet in hostinfo_sheets:
            for hostinfo in sheet:
                if re.findall(part_of_host, hostinfo.name):
                    iplist_hostinfos.append(hostinfo)

        if iplist_hostinfos:
            new_iplist_infos[iplist] = iplist_hostinfos

    if not new_iplist_infos:
        print('No target hosts were found.')
        sys.exit(1)

    return new_iplist_infos


def get_target_hostinfo(hostname, search_iplist):
    """
    Get target host info.
    """

    if search_iplist:
        all_hostinfos = search.get_all_hostinfos()
        if not all_hostinfos:
            print('Host information are nothing.')
            sys.exit(1)

        iplist_infos = _sepalate_hitting_host(all_hostinfos, hostname)
        target_hostinfo = _print_choose_targethost(iplist_infos)
    else:
        target_hostinfo = search.get_target_hostinfo(hostname)

    return target_hostinfo
