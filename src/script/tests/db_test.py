#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import MySQLdb
import string
import random


def connection(host, user, password, db):
    return MySQLdb.connect(host=host,
                           user=user,
                           passwd=password,
                           db=db)


conn = connection(host="localhost", user="root", password="123456", db="test")


def make_phone():
    phone = [random.choice(string.digits) for i in range(13)]
    return "".join(phone)


def make_name():
    name = [random.choice(string.ascii_letters) for i in range(15)]
    return "".join(name)


def make_agent():
    agent = dict()
    agent["phone"] = make_phone()
    agent["name"] = make_name()
    agent["agent_id"] = random.randint(0, 99999999)
    return agent


def make_agent_use_log(agent_id, phone, name):
    agent_use_log = dict()
    agent_use_log["agent_id"] = agent_id
    agent_use_log["phone"] = phone
    agent_use_log["name"] = name
    return agent_use_log


def make_org_billing_log(log_id, agent_id):
    org_billing_log = dict()
    org_billing_log["log_id"] = log_id
    org_billing_log["agent_id"] = agent_id
    org_billing_log["admin_id"] = random.randint(0, 99999999)
    org_billing_log["top_org_id"] = random.randint(0, 99999999)
    org_billing_log["type"] = 'AgentUse'
    return org_billing_log


def save_agent_info(agent_info):
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO `agent` (`agent_id`, `phone`, `name`)
        VALUES (%s, %s, %s)
    """, (agent_info["agent_id"], agent_info["phone"], agent_info["name"]))
    conn.commit()
    cur.close()


def save_agent_use_log(agent_use_log):
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO `agent_use_log`(`agent_id`, `phone`, `name`)
        VALUES (%s, %s, %s)
    """, [agent_use_log["agent_id"], agent_use_log["phone"], agent_use_log["name"]])
    conn.commit()
    log_id = cur.lastrowid
    cur.close()
    return log_id


def save_billing_log(billing_log):
    cur = conn.cursor()
    cur.execute("""
            INSERT INTO `org_billing_log`(`log_id`, `agent_id`, `admin_id`, `top_org_id`, `type`)
            VALUES (%s, %s, %s, %s, %s)
        """, [billing_log["log_id"], billing_log["agent_id"], billing_log["admin_id"], billing_log["top_org_id"],
              billing_log["type"]])
    conn.commit()
    cur.close()


def get_agent():
    cur = conn.cursor()
    cur.execute("""
        SELECT `agent_id`, `phone`, `name` FROM `agent`
    """)
    rows = cur.fetchall()
    cur.close()
    return rows


def main():
    agents = get_agent()
    for i in range(100000):
        agent = agents[i]
        agent_use_log = make_agent_use_log(agent[0], agent[1], agent[2])
        log_id = save_agent_use_log(agent_use_log)
        billing_log = make_org_billing_log(log_id, agent[0])
        save_billing_log(billing_log)


if __name__ == "__main__":
    main()
