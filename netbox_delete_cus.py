#!/usr/bin/python3
__author__ = "nosue4it"
__author_email__ = "github@schlueter-online.net"
__copyright__ = "Copyright (c) 2023 nouse4it"

"""
Category: Netbox Automation
Author: nouse4it <github@schlueter-online.net>

netbox_fw_ips.py
Illustrate the following concepts:
- Reserve IPs for Tenant FW depent on the provided FW solutions model

"""

# Importing all needed Modules
import pynetbox
import sys

nb = pynetbox.api(url=sys.argv[1], token=sys.argv[2])

# CUS ID of Customer, for which TCO should be implemented
# Normally comes from Jarvis API
cus_code = f'{sys.argv[3]}01'.upper()

# Get Customer Tenant ID
cus_ten_id = nb.tenancy.tenants.get(name=f"{cus_code}").id

# ==============================================================================
# Get IDs for IP addresses used in Tenant and delete them


def delete_ips_cus(cus_ten_id):
    ips = nb.ipam.ip_addresses.filter(tenant_id=cus_ten_id)
    ips_to_delete = []
    for ip in ips:
        ips_to_delete.append(ip.id)
    nb.ipam.ip_addresses.delete(ips_to_delete)
# ==============================================================================
# ==============================================================================
# Get IDs for Route-Targets used in Tenant and delete them


def delete_rts_cus(cus_ten_id):
    rts = nb.ipam.route_targets.filter(tenant_id=cus_ten_id)
    rts_to_delete = []
    for rt in rts:
        rts_to_delete.append(rt.id)
    nb.ipam.route_targets.delete(rts_to_delete)
# ==============================================================================
# ==============================================================================
# Get IDs for Prefixes used in Tenant and delete them


def delete_prefixes_cus(cus_ten_id):
    prefixes = nb.ipam.prefixes.filter(tenant_id=cus_ten_id)
    prefixes_to_delete = []
    for prefix in prefixes:
        prefixes_to_delete.append(prefix.id)
    nb.ipam.prefixes.delete(prefixes_to_delete)
# ==============================================================================
# ==============================================================================
# Get IDs for VLANs used in Tenant and delete them


def delete_vlans_cus(cus_ten_id):
    vlans = nb.ipam.vlans.filter(tenant_id=cus_ten_id)
    vlans_to_delete = []
    for vlan in vlans:
        vlans_to_delete.append(vlan.id)
    nb.ipam.vlans.delete(vlans_to_delete)
# ==============================================================================
# ==============================================================================
# Get IDs for VRFs used in Tenant and delete them


def delete_vrfs_cus(cus_ten_id):
    vrfs = nb.ipam.vrfs.filter(tenant_id=cus_ten_id)
    vrfs_to_delete = []
    for vrf in vrfs:
        vrfs_to_delete.append(vrf.id)
    nb.ipam.vrfs.delete(vrfs_to_delete)
# ==============================================================================
# ==============================================================================
# Get IDs for VRFs used in Tenant and delete them


def delete_tenant_cus(cus_ten_id):
    nb.tenancy.delete(cus_ten_id)
# ==============================================================================


# ==============================================================================
# Main
delete_ips_cus(cus_ten_id)
delete_rts_cus(cus_ten_id)
delete_prefixes_cus(cus_ten_id)
delete_vlans_cus(cus_ten_id)
delete_vrfs_cus(cus_ten_id)
delete_tenant_cus(cus_ten_id)
