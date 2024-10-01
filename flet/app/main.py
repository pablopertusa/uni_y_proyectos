import flet as ft
from flet import icons
import datetime
import sqlite3 as sql
import time
import random
import pandas as pd


# DATABASE ---------------------------------------------------------------------


def connect_db():
    global conn 
    conn = sql.connect("app_database.db")
    conn.execute('PRAGMA foreign_keys = ON')
    global cursor 
    cursor = conn.cursor()    
    cursor.execute("CREATE TABLE IF NOT EXISTS productos (id TEXT PRIMARY KEY, nombre TEXT, marca TEXT, prenda TEXT, temporada TEXT, color TEXT, precio REAL, stock INTEGER, descripcion TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS acciones (id TEXT PRIMARY KEY, product_id TEXT, accion TEXT, fecha TEXT, cantidad INTEGER, coste REAL, FOREIGN KEY (product_id) REFERENCES productos(id) ON DELETE CASCADE ON UPDATE NO ACTION)")
    conn.commit()
    return conn, cursor

def name_query(name):
    cursor.execute(f"SELECT * FROM productos WHERE nombre LIKE '%{name}%'")
    return cursor.fetchall()
    
def brand_query(brand):
    cursor.execute(f"SELECT * FROM productos WHERE marca LIKE '%{brand}%'")
    return cursor.fetchall()

def season_query(season):
    cursor.execute(f"SELECT * FROM productos WHERE temporada LIKE '%{season}%'")
    return cursor.fetchall()
    
def color_query(color):
    cursor.execute(f"SELECT * FROM productos WHERE color LIKE '%{color}%'")
    return cursor.fetchall()

def type_query(type):
    cursor.execute(f"SELECT * FROM productos WHERE prenda LIKE '%{type}%'")
    return cursor.fetchall()

def id_query(id):
    cursor.execute(f"SELECT * FROM productos WHERE id = '{id}'")
    return cursor.fetchone()

def how_many(product_id):
    cursor.execute(f"SELECT stock FROM productos WHERE id = '{product_id}'")
    return cursor.fetchone()[0]

def new_product(product_name, marca="", prenda="", temporada="", color="", precio="", stock="", descripcion=""):
    
    if product_name == "": return False
    
    if precio != "":
        precio = float(precio)
    else:
        precio = None
    if stock != "":
        stock = int(stock)
    else:
        stock = 0

    try:
        id = product_name
        cursor.execute('''INSERT INTO productos (id, nombre, marca, prenda, temporada, color, precio, stock, descripcion) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', (id, product_name, marca, prenda, temporada, color, precio, stock, descripcion))
        conn.commit()
        return True
    except Exception as e:
        print(e)
        return False
    
def delete_product(product_id):
    try:
        cursor.execute(f"DELETE FROM productos WHERE id = '{product_id}'")
        conn.commit()
        return True
    except Exception as e:
        print(e)
        return False
    
    
def new_action(product_id, action, date, quantity, cost):
    if quantity == "":
        return False, "Cantidad no puede estar vacío"
    
    if product_id == "":
        return False, "Producto no puede estar vacío"

    stock = how_many(product_id)
    
    if action == "venta" and int(quantity) > stock:
        return False, "No hay suficiente stock"
    
    if date == "Fecha":
        date = "No registrada"
    
    try:
        id = "accion" + str(random.randint(1, 1000000000))
        cursor.execute('''INSERT INTO acciones (id, product_id, accion, fecha, cantidad, coste) VALUES (?, ?, ?, ?, ?, ?)''', (id, product_id, action, date, quantity, cost))
        if action == "venta":
            cursor.execute(f"UPDATE productos SET stock = {stock - int(quantity)} WHERE id = '{product_id}'")
            conn.commit()
            return True, "Venta registrada correctamente"
        else:
            cursor.execute(f"UPDATE productos SET stock = {stock + int(quantity)} WHERE id = '{product_id}'")
            conn.commit()
            return True, "Compra registrada correctamente"
    except Exception as e:
        print(e)
        if action == "venta":
            return False, "Error al registrar venta"
        else:    
            return False, "Error al registrar compra"
    
    
def all_products():
    cursor.execute("SELECT * FROM productos")
    return cursor.fetchall()

def query_by(filter, value):
    if filter == "Nombre":
        return name_query(value)
    elif filter == "Marca":
        return brand_query(value)
    elif filter == "Temporada":
        return season_query(value)
    elif filter == "Color":
        return color_query(value)
    elif filter == "Prenda":
        return type_query(value)
    else:
        return all_products()
    


def download_db(open_snackbar):
    
    try:
        
        output_file = "base_datos.xlsx"
        writer = pd.ExcelWriter(output_file, engine='openpyxl')
        
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tablas = cursor.fetchall()
        
        for tabla in tablas:
            nombre_tabla = tabla[0]
            df = pd.read_sql_query(f"SELECT * FROM {nombre_tabla}", conn)
            df.to_excel(writer, sheet_name=nombre_tabla, index=False)
        
        writer._save()
        
        open_snackbar("Base de datos descargada correctamente", "green")
        
        return True
    
    except Exception as e:
        print(e)
        open_snackbar("Error al descargar base de datos", "red")
        return False
    
    
    
    
'''
    
def obtener_ventas_compras(cursor):
    # Obtener el mes y año actual
    fecha_actual = datetime.now()
    
    # Calcular la fecha de inicio (3 meses atrás desde el primer día del mes actual)
    fecha_inicio = fecha_actual.replace(day=1) - timedelta(days=90)
    
    # Calcular la fecha de fin (final del mes actual)
    fecha_fin = fecha_actual.replace(day=1) + timedelta(days=32)
    fecha_fin = fecha_fin.replace(day=1) - timedelta(days=1)
    
    # Formatear fechas en el formato DD-MM-YYYY para la consulta
    fecha_inicio_str = fecha_inicio.strftime("%d-%m-%Y")
    fecha_fin_str = fecha_fin.strftime("%d-%m-%Y")

    # Consulta SQL
    query = """
    SELECT accion, SUM(cantidad) as total_cantidad, SUM(coste) as total_coste
    FROM acciones
    WHERE strftime('%s', substr(fecha, 7, 4) || '-' || substr(fecha, 4, 2) || '-' || substr(fecha, 1, 2)) 
          BETWEEN strftime('%s', ?) AND strftime('%s', ?)
    GROUP BY accion
    """
    
    # Ejecutar la consulta
    cursor.execute(query, (fecha_inicio_str, fecha_fin_str))
    
    # Obtener los resultados
    resultados = cursor.fetchall()
    
    # Formatear los resultados
    ventas = {"cantidad": 0, "coste": 0.0}
    compras = {"cantidad": 0, "coste": 0.0}
    
    for row in resultados:
        if row[0] == "venta":
            ventas["cantidad"] = row[1]
            ventas["coste"] = row[2]
        elif row[0] == "compra":
            compras["cantidad"] = row[1]
            compras["coste"] = row[2]
    
    return {"ventas": ventas, "compras": compras}


def graficar_ventas_compras(resultados):
    categorias = ['Ventas', 'Compras']
    cantidades = [resultados['ventas']['cantidad'], resultados['compras']['cantidad']]
    costes = [resultados['ventas']['coste'], resultados['compras']['coste']]

    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('Categorías')
    ax1.set_ylabel('Cantidad', color=color)
    ax1.bar(categorias, cantidades, color=color, alpha=0.6, label='Cantidad')
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('Coste', color=color)
    ax2.plot(categorias, costes, color=color, marker='o', label='Coste')
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()
    plt.title('Ventas y Compras en los Últimos 3 Meses')

'''


# NAVIGATION BAR ---------------------------------------------------------------

class customNavigationBar(ft.NavigationBar):
    def __init__(self, on_change_function):
        super().__init__()
        #self.bgcolor = "#03346E"
        self.on_change = on_change_function
        self.adaptive = True
        self.bgcolor = "#97deff"
        self.selected_index = 0
        self.indicator_color = "white"
        self.destinations = [
            ft.NavigationBarDestination(label = "Productos", icon="shopping_cart"),
            ft.NavigationBarDestination("Acciones", icon=icons.ATTACH_MONEY),
            ft.NavigationBarDestination("Base de datos", icon=icons.INFO),
        ]
        
        
# PESTAÑA DE PRODUCTOS --------------------------------------------------------


class editModalContent(ft.Column):
    def __init__(self, product_id):
        super().__init__()
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.width = 500
        self.controls.append(ft.Divider(height=25, color="transparent"))
        marca, prenda, temporada, color, precio, stock, descripcion = id_query(product_id)[2:]
        self.new_marca = ft.TextField(label="Marca", width=220, border_color="grey",value=marca)
        self.new_prenda = ft.TextField(label="Prenda", width=220, border_color="grey", value=prenda)
        self.controls.append(ft.Row([self.new_marca, self.new_prenda], spacing=20, vertical_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER))
        self.new_temporada = ft.TextField(label="Temporada", width=220, border_color="grey", value=temporada)
        self.new_color = ft.TextField(label="Color", width=220, border_color="grey", value=color)
        self.controls.append(ft.Row([self.new_temporada, self.new_color], spacing=20, vertical_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER))
        self.new_precio = ft.TextField(label="Precio de venta", width=140, border_color="grey", suffix_text="€", input_filter=ft.InputFilter(allow=True, regex_string=r"[\d.]", replacement_string=""), value=precio)
        self.new_stock = ft.TextField(label="Stock", width=140, border_color="grey", suffix_text="unidades", input_filter=ft.NumbersOnlyInputFilter(), value=stock)
        self.controls.append(ft.Row([self.new_precio, self.new_stock], spacing=20, vertical_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER))
        self.new_descripcion = ft.TextField(label="Descripción", width=450, border_color="grey", multiline=True, min_lines=3, value=descripcion)
        self.controls.append(self.new_descripcion)
        self.spacing = 25

class customDropDown(ft.Dropdown):
    def __init__(self):
        super().__init__()
        self.options = [ft.dropdown.Option("Nombre"), ft.dropdown.Option("Marca"), ft.dropdown.Option("Temporada"), ft.dropdown.Option("Color"), ft.dropdown.Option("Prenda")]    
        self.on_change = lambda e: print(e.control.value)
        self.label = "FIltrar por"
        self.width = 200


class addProductTab(ft.Tab):
    def __init__(self):
        super().__init__()
        self.text = "Nuevo  "
        self.icon = icons.ADD
        
class searchProductTab(ft.Tab):
    def __init__(self):
        super().__init__()
        self.text = "Buscar  "
        self.icon = icons.SEARCH
        


class addProductTabContent(ft.Column):
    def __init__(self, open_snackbar):
        super().__init__()
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER    
        self.open_snackbar = open_snackbar    
        self.controls.append(ft.Divider(height=20, color="transparent"))
        self.nombre_producto = ft.TextField(label="Nombre del producto", width=500, border_color="grey", autofocus=True, suffix_text="Obligatorio")
        self.controls.append(self.nombre_producto)
        self.marca_producto = ft.TextField(label="Marca", width=300, border_color="grey")
        self.prenda_producto = ft.TextField(label="Prenda", width=300, border_color="grey")
        self.controls.append(ft.Row([self.marca_producto, self.prenda_producto], spacing=20, vertical_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER))
        self.temporada_producto = ft.TextField(label="Temporada", width=300, border_color="grey")
        self.color_producto = ft.TextField(label="Color", width=300, border_color="grey")
        self.controls.append(ft.Row([self.temporada_producto, self.color_producto], spacing=20, vertical_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER))
        self.precio_producto = ft.TextField(label="Precio de venta", width=200, border_color="grey", suffix_text="€", input_filter=ft.InputFilter(allow=True, regex_string=r"[\d.]", replacement_string=""))
        self.stock_producto = ft.TextField(label="Stock inicial", width=200, border_color="grey", suffix_text="unidades", input_filter=ft.NumbersOnlyInputFilter())
        self.controls.append(ft.Row([self.precio_producto, self.stock_producto], spacing=20, vertical_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER))
        self.descripcion_producto = ft.TextField(label="Descripción", width=550, border_color="grey", multiline=True, min_lines=3)
        self.controls.append(self.descripcion_producto)
        self.controls.append(ft.FilledButton("Añadir producto", on_click=lambda e: self.add_product(), height=50, adaptive=True, icon=icons.ADD))
        self.spacing = 25
        
    def add_product(self):
        print(self.precio_producto.value, type(self.precio_producto.value))
        if new_product(self.nombre_producto.value, self.marca_producto.value, self.prenda_producto.value, self.temporada_producto.value, self.color_producto.value, self.precio_producto.value, self.stock_producto.value, self.descripcion_producto.value):
            self.open_snackbar("Producto agregado correctamente", "green")
        else:
            self.open_snackbar("Error al agregar producto. Prueba a cambiar el nombre del producto", "red")
        

        
class searchProductTabContent(ft.Column):
    def __init__(self, open_snackbar, edit_modal, change_height):
        super().__init__()
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.controls.append(ft.Divider(height=20, color="transparent"))
        self.results = []
        
        class customCard(ft.Card):
            def __init__(self, product_id, open_snackbar, dropdown, textField):
                super().__init__()
                self.product_id = product_id
                #self.color = "black"
                id, name, brand, type, season, color, price, stock, description = id_query(product_id)
                if price == None:
                    price = "No registrado"
                else:
                    price = f"{price} €"
                self.open_snackbar = open_snackbar
                self.dropdown = dropdown
                self.textField = textField
                self.content = ft.Container(
                    content=ft.Column(
                        [
                            ft.ListTile(
                                leading=ft.Icon(icons.STOREFRONT),
                                title=ft.Text(f"Producto {self.product_id} - {brand} {type} {season} {color}"),
                                subtitle=ft.Text(f"Stock: {stock} unidades, Precio: {price}"),
                            ),
                            ft.Row(
                                [ft.TextButton("Editar", on_click=lambda e: edit_modal(product_id)), ft.IconButton(icon=icons.DELETE, icon_color="red", on_click=lambda e: self.delete_card())],
                                alignment=ft.MainAxisAlignment.END,
                            ),
                        ]
                    ),
                    width=600,
                    padding=10,
                )
                
            def delete_card(self):
                if delete_product(self.product_id):
                    show_cards(self.dropdown.value, self.textField.value)
                    self.open_snackbar("Producto eliminado correctamente", "green")
                else:
                    self.open_snackbar("Error al eliminar producto", "red")
                    
        
        def show_cards(filter, value):
            self.controls = self.controls[:3]
            self.update()
            self.results = query_by(filter, value)
            
            if len(self.results) > 2:
                height = 600 + 140 * (len(self.results) - 2)
                change_height(height)
            else:
                change_height(600)
                
            num_cards = len(self.results)
            for i in range(num_cards):
                self.controls.append(customCard(self.results[i][0], open_snackbar, self.dropdown, self.textField))
            self.update()
        
        self.dropdown = customDropDown()
        self.textField = ft.TextField(label="Buscar producto", width=350, border_color="grey", autofocus=True)
        self.controls.append(ft.Row([self.dropdown, self.textField, ft.FloatingActionButton(icon="search", on_click=lambda e: show_cards(self.dropdown.value, self.textField.value), height=50)], spacing=20, vertical_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER))
        self.controls.append(ft.Divider(height=20, color="transparent"))
        
        
        
class ProductsColumn(ft.Column):
    def __init__(self, open_snackbar, edit_modal):
        super().__init__()
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.height = 600
        self.add_tab = addProductTab()
        self.search_tab = searchProductTab()
        self.add_tab.content = addProductTabContent(open_snackbar)
        self.search_tab.content = searchProductTabContent(open_snackbar, edit_modal, self.change_height)
        self.controls.append(ft.Tabs([self.add_tab, self.search_tab], tab_alignment=ft.TabAlignment.CENTER, on_change=lambda e: self.on_change_tab(), animation_duration=1, selected_index=1))
        
    def change_height(self, height):
        self.height = height
        self.update()
        
    def on_change_tab(self):
        if self.controls[0].selected_index == 0:
            self.change_height(600)
        else:
            results = self.search_tab.content.results
            if len(results) > 2:
                height = 600 + 140 * (len(results) - 2)
                self.change_height(height)
            else:
                self.change_height(600)
            
        
        
# PESTAÑA DE ACCIONES ------------------------------------------------------------

class customSearchBar(ft.SearchBar):
    def __init__(self):
        super().__init__()
        self.bar_hint_text = "Buscar producto"
        self.view_hint_text = "Elige un producto"
        self.on_tap = lambda e: self.open_view()
        self.products = all_products()
        self.products.sort(key=lambda x: x[1])
        self.controls = [
            ft.ListTile(title=ft.Text(f"Producto {i[1]} - {i[3]} {i[2]} {i[5]}"), on_click=lambda e: self.close_view(e.control.data), data=i[1])
            for i in self.products
        ]
        
        
class buyTabContent(ft.Column):
    def __init__(self, open_date_picker, open_snackbar):
        super().__init__()
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.controls.append(ft.Divider(height=35, color="transparent"))  
        self.controls.append(customSearchBar())
        self.controls.append(ft.Divider(height=35, color="transparent"))
        self.cantidad = ft.TextField(label="Cantidad", width=200, border_color="grey", suffix_text="unidades", input_filter=ft.NumbersOnlyInputFilter())
        self.coste = ft.TextField(label="Coste total de compra", width=200, border_color="grey", suffix_text="€", input_filter=ft.InputFilter(allow=True, regex_string=r"[\d.]", replacement_string=""))
        self.fecha = ft.OutlinedButton("Fecha", on_click=lambda e: open_date_picker(e), icon=icons.CALENDAR_MONTH, height=50, width=200)
        self.controls.append(ft.Row([self.cantidad, self.coste, self.fecha], spacing=20, vertical_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER))
        self.controls.append(ft.Divider(height=30, color="transparent"))
        self.controls.append(ft.FilledButton("Registrar compra", height=60, width=200, icon=icons.ATTACH_MONEY, on_click=lambda e: register_buy()))
        
        def register_buy():
            result, text = new_action(self.controls[1].value, "compra", self.fecha.text, self.cantidad.value, self.coste.value)
            print(self.fecha.text)
            if result:
                open_snackbar(text, "green")
            else:
                open_snackbar(text, "red")
        
class sellTabContent(ft.Column):
    def __init__(self, open_date_picker, open_snackbar):
        super().__init__()
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.controls.append(ft.Divider(height=35, color="transparent"))  
        self.controls.append(customSearchBar())
        self.controls.append(ft.Divider(height=35, color="transparent"))
        self.cantidad = ft.TextField(label="Cantidad", width=200, border_color="grey", suffix_text="unidades", input_filter=ft.NumbersOnlyInputFilter())
        self.coste = ft.TextField(label="Coste total de venta", width=200, border_color="grey", suffix_text="€", input_filter=ft.InputFilter(allow=True, regex_string=r"[\d.]", replacement_string=""))
        self.fecha = ft.OutlinedButton("Fecha", on_click=lambda e: open_date_picker(e), icon=icons.CALENDAR_MONTH, height=50, width=200)
        self.controls.append(ft.Row([self.cantidad, self.coste, self.fecha], spacing=20, vertical_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER))
        self.controls.append(ft.Divider(height=30, color="transparent"))
        self.controls.append(ft.FilledButton("Registrar venta", height=60, width=200, icon=icons.SELL_OUTLINED, on_click=lambda e: register_sell()))
        
        def register_sell():
            result, text = new_action(self.controls[1].value, "venta", self.fecha.text, self.cantidad.value, self.coste.value)
            if result:
                open_snackbar(text, "green")
            else:
                open_snackbar(text, "red")
        

class buyTab(ft.Tab):
    def __init__(self, open_date_picker, open_snackbar):
        super().__init__()
        self.text = "Compra  "
        self.icon = icons.ATTACH_MONEY
        self.content = buyTabContent(open_date_picker, open_snackbar)

class sellTab(ft.Tab):
    def __init__(self, open_date_picker, open_snackbar):
        super().__init__()
        self.text = "Venta  "
        self.icon = icons.SELL_OUTLINED
        self.content = sellTabContent(open_date_picker, open_snackbar)
        
        
        
class ActionsColumn(ft.Column):
    def __init__(self, open_date_picker, open_snackbar):
        super().__init__()
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.height = 600
        self.buy_tab = buyTab(open_date_picker, open_snackbar)
        self.sell_tab = sellTab(open_date_picker, open_snackbar)
        self.controls.append(ft.Tabs([self.buy_tab, self.sell_tab], tab_alignment=ft.TabAlignment.CENTER, on_change=lambda e: print(e.control.selected_index), animation_duration=1, selected_index=0))

# PESTAÑA DE INFORMACIÓN --------------------------------------------------------



class infoColumn(ft.Column):
    def __init__(self, download_db, open_snackbar):
        super().__init__()
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.controls.append(ft.Divider(height=170, color="transparent"))
        '''
        self.controls.append(ft.Text("¿Cómo va la tienda?", size=30, weight=ft.FontWeight.BOLD))
        animation = ft.Lottie(src=f"https://lottie.host/61cfb7bf-32b1-4fbc-8e51-d9af26a869ee/UzpKm7dBvl.json", width=400, height=400, animate=True, fit=ft.ImageFit.CONTAIN)
        self.controls.append(animation)
        self.controls.append(ft.Divider(height=20, color="transparent"))
        '''
        self.controls.append(ft.Text("Descargar base de datos", size=30, weight=ft.FontWeight.BOLD))
        self.controls.append(ft.Divider(height=20, color="transparent"))
        self.controls.append(downloadButton(download_db, open_snackbar))
        #chart = graficar_ventas_compras(obtener_ventas_compras(cursor))
        #self.controls.append(MatplotlibChart(chart))
        

# BOTON DESCARGAR BASE DE DATOS ------------------------------------------------

class downloadButton(ft.FloatingActionButton):
    def __init__(self, download_db, open_snackbar):
        super().__init__()
        self.icon = icons.DOWNLOAD
        self.on_click = lambda e: download_db(open_snackbar)
        self.bgcolor = ft.colors.LIME_300


# MAIN -----------------------------------------------------------------------------

def main(page):
    
    def change_date_button(date):
        if actions_column.controls[0].selected_index == 0:
            actions_column.buy_tab.content.fecha.text = date
            page.update()
        else:
            actions_column.sell_tab.content.fecha.text = date
            page.update()
        
        
    def open_date_picker(e):
        page.open(ft.DatePicker(first_date=datetime.datetime(year=2020, month=10, day=1),
            on_change=lambda e: change_date_button(e.control.value.strftime('%d-%m-%Y')),
            on_dismiss=lambda e: print("DatePicker dismissed"),
            cancel_text="Cancelar"
        ))
    
    def on_change(event):
        index = nav.selected_index
        if index == 0:
            print("Productos")
            page.controls.pop()
            page.add(ProductsColumn(open_snackbar, edit_modal))
        elif index == 1:
            page.controls.pop()
            global actions_column
            actions_column = ActionsColumn(open_date_picker, open_snackbar)
            page.add(actions_column)
            print("Acciones")
            
        elif index == 2:
            print("Información")
            page.controls.pop()
            page.add(infoColumn(download_db, open_snackbar))
        
        page.update()
        
    def open_snackbar(text, color):
        snackbar.content = ft.Text(text, color="white")
        snackbar.bgcolor = color
        snackbar.open = True
        page.update()
        
    def update_product(product_id, new_marca, new_prenda, new_temporada, new_color, new_precio, new_stock, new_descripcion):
        
        if new_precio != "":
            new_precio = float(new_precio)
        else:
            new_precio = None
        if new_stock != "":
            new_stock = int(new_stock)
        else:
            new_stock = None
        try:
            cursor.execute('''UPDATE productos SET marca = ?, prenda = ?, temporada = ?, color = ?, precio = ?, stock = ?, descripcion = ? WHERE id = ?''', (new_marca, new_prenda, new_temporada, new_color, new_precio, new_stock, new_descripcion, product_id))
            conn.commit()
            return True
        except Exception as e:
            print(e)
            return False
        
    def confirm_update(modal_dialog, product_id, new_marca, new_prenda, new_temporada, new_color, new_precio, new_stock, new_descripcion):
        result = update_product(product_id, new_marca, new_prenda, new_temporada, new_color, new_precio, new_stock, new_descripcion)
        if result:
            page.close(modal_dialog)
            open_snackbar("Producto actualizado correctamente", "green")
        else:
            page.close(modal_dialog)
            open_snackbar("Error al actualizar producto", "red")
        
    def edit_modal(product_id):
        modal_dialog = ft.AlertDialog(
            modal=True,
            icon=ft.Icon(icons.EDIT),
            title=ft.Text("Editar producto", text_align=ft.TextAlign.CENTER),
            content=editModalContent(product_id),
            actions=[
                ft.TextButton("Confirmar", on_click=lambda e: confirm_update(modal_dialog, product_id, new_marca.value, new_prenda.value, new_temporada.value, new_color.value, new_precio.value, new_stock.value, new_descripcion.value), height=50),
                ft.TextButton("Cancelar", on_click=lambda e: page.close(modal_dialog), height=50),
            ],
            actions_alignment=ft.MainAxisAlignment.END
        )
        new_marca = modal_dialog.content.new_marca
        new_prenda = modal_dialog.content.new_prenda
        new_temporada = modal_dialog.content.new_temporada
        new_color = modal_dialog.content.new_color
        new_precio = modal_dialog.content.new_precio
        new_stock = modal_dialog.content.new_stock
        new_descripcion = modal_dialog.content.new_descripcion
        page.open(modal_dialog)
        
        
    page.title = "Panel de control"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.maximized = True
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    #progress_bar = ft.ProgressBar(width=400, color="blue", bgcolor="#eeeeee")
    #page.add(progress_bar)
    
    customLottie = ft.Lottie(
        src='https://lottie.host/46efe719-d087-469b-9cb2-aaafab0051b1/JXYbtGzM6y.json',
        repeat=True,
        expand=True,
        fit=ft.ImageFit.CONTAIN,
        animate=True,
    )
    page.add(customLottie)
    
    for i in range(3):
        if i == 0:
            page.add(ft.Text("Cargando interfaz..."))
        elif i == 1:
            page.controls.pop()
            page.add(ft.Text("Cargando herramientas..."))
            connect_db()
        else:
            page.controls.pop()
            page.add(ft.Text("Cargando base de datos..."))
        time.sleep(2.5)
        
    page.controls.pop()
    page.controls.pop()
    page.scroll = ft.ScrollMode.AUTO
    nav = customNavigationBar(on_change)
    page.navigation_bar = nav
    page.add(ProductsColumn(open_snackbar, edit_modal))
    snackbar = ft.SnackBar(ft.Text(), behavior=ft.SnackBarBehavior.FLOATING, margin=0, duration=5000)
    page.overlay.append(snackbar)
    page.update()
    



ft.app(target=main)