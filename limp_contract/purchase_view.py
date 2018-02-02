<record id="purchase_order_form" model="ir.ui.view">
            <field name="name">purchase.order.form</field>
            <field name="model">purchase.order</field>
            <field name="type">form</field>
            <field name="arch" type="xml">
                <form string="Purchase Order">
                    <group col="6" colspan="4">
                        <field name="name"/>
                        <field name="date_order"/>
                        <field name="invoiced"/>
                        <newline/>
                        <field name="warehouse_id" on_change="onchange_warehouse_id(warehouse_id)" widget="selection"/>
                        <field name="partner_ref"/>
                        <field name="shipped"/>
                        <field name="company_id" groups="base.group_multi_company" widget="selection"/>
                    </group>
                    <notebook colspan="4">
                        <page string="Purchase Order">
                            <field name="partner_id" on_change="onchange_partner_id(partner_id)" context="{'search_default_supplier':1}" />
                            <field name="partner_address_id"/>
                            <field domain="[('type','=','purchase')]" name="pricelist_id" groups="base.group_extended"/>
                            <field name="origin" groups="base.group_extended"/>
                            <newline/>
                            <field colspan="4" name="order_line" nolabel="1" mode="tree,form">
                                <tree string="Purchase Order Lines">
                                    <field name="date_planned"/>
                                    <field name="name"/>
                                    <field name="product_qty"/>
                                    <field name="product_uom"/>
                                    <field name="price_unit"/>
                                    <field name="price_subtotal"/>
                                </tree>
                                <!-- default form view -->
                            </field>
                            <group col="7" colspan="4">
                                <field name="amount_untaxed" sum="Untaxed amount"/>
                                <field name="amount_tax"/>
                                <field name="amount_total" sum="Total amount"/>
                                <button name="button_dummy" states="draft" string="Compute" type="object" icon="gtk-execute"/>
                            </group>
                            <group col="11" colspan="4">
                                <field name="state" readonly="1"/>
                                <button name="purchase_cancel" states="draft,confirmed,wait_auth" string="Cancel" icon="gtk-cancel"/>
                                <button name="action_cancel_draft" states="cancel" string="Set to Draft" type="object" icon="gtk-convert"/>
                                <button name="action_cancel" states="approved,except_picking,except_invoice,wait" string="Cancel Purchase Order" type="object" icon="gtk-cancel"/>
                                <button name="picking_ok" states="except_picking" string="Manually Corrected" icon="gtk-convert"/>
                                <button name="invoice_ok" states="except_invoice" string="Manually Corrected" icon="gtk-convert"/>
                                <button name="purchase_confirm" states="draft" string="Convert to Purchase Order" icon="gtk-go-forward"/>
                                <button name="purchase_appbuyer" states="wait_auth" string="Approve Purchase" icon="gtk-ok"/>
                                <button name="purchase_approve" states="confirmed" string="Approved" icon="gtk-go-forward"/>
                                <button name="%(report_purchase_order)d" string="Print" states="approved" type="action" icon="gtk-print"/>
                            </group>
                        </page>
                        <page string="Delivery &amp; Invoicing" groups="base.group_extended">
                            <group colspan="2" col="2">
                                <separator string="Delivery" colspan="2"/>
                                <field name="dest_address_id" on_change="onchange_dest_address_id(dest_address_id)"/>
                                <field name="minimum_planned_date"/>
                                <field name="location_id"/>
                            </group>
                            <group colspan="2" col="2">
                                <separator string="Invoice Control" colspan="2"/>
                                <field name="invoice_method"/>
                                <field name="fiscal_position" widget="selection"/>
                            </group>
                            <newline/>
                            <separator string="Purchase Control" colspan="4"/>
                            <field name="validator"/>
                            <field name="date_approve"/>
                                <separator string="Invoices" colspan="4"/>
                                <newline/>
                                <field name="invoice_ids" groups="base.group_extended" nolabel="1" colspan="4" context="{'type':'in_invoice', 'journal_type': 'purchase'}"/>
                        </page>
                        <page string="Notes">
                            <field colspan="4" name="notes" nolabel="1"/>
                        </page>
                    </notebook>
                </form>
            </field>
        </record>
