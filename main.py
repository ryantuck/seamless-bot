# calculate who owes what. yey.

import json

# load configs
with open('menu.json') as f:
    menu = json.load(f)
with open('orders/2016-06-22.json') as f:
    order = json.load(f)

# compute subtotals of all items purchased
print '============================================'
print 'order'
print '--------------------------------------------'
owed = {}
for person, items in order['people'].iteritems():

    print person
    subtotal = 0
    for item_id, item_qty in items.iteritems():

        item = menu[item_id]
        item_total = item_qty * item['price']

        print '\t', format(item_total, '.2f'), '\t', item_qty, 'x', item['better_name']
        subtotal += item_total
    print '\t', format(subtotal, '.2f'), '\t', 'total'

    owed[person] = subtotal

# spread tax and tip based on percentage of total
print '============================================'
print 'totals owed (+ tax n tip)'
print '--------------------------------------------'
pre_tax_tip_subtotal = sum(owed.values())
tax_n_tip = order['tax'] + order['tip']
for person, value in owed.iteritems():
    owed[person] += (value / pre_tax_tip_subtotal) * tax_n_tip
    print person, '\t\t', format(owed[person], '.2f')

# print summary
total = sum(owed.values())
print '============================================'
print 'order summary'
print '--------------------------------------------'
print 'subtotal:', '\t', format(pre_tax_tip_subtotal, '.2f')
print 'tax/tip:', '\t', format(tax_n_tip, '.2f')
print 'total:', '\t\t', format(total, '.2f')
