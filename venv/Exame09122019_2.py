import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
class Exame(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Exame 9-12-2019")
        self.set_border_width(10)
        caixaV = Gtk.Box (orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(caixaV)
        lblNome = Gtk.Label("Nome:")
        lblApelido = Gtk.Label("Apelido:")
        lblTratamento = Gtk.Label("Tratamento:")
        lblNomeUsuario= Gtk.Label ("Nome de Usuario:")
        lblFormato = Gtk.Label("Formato:")
        txtNome= Gtk.Entry()
        txtApelido= Gtk.Entry()
        txtTratamento= Gtk.Entry()
        txtNomeUsuario= Gtk.Entry()
        cmbFormato=Gtk.ComboBoxText()

        #Añadir controles que no aparecen (1)
        grid = Gtk.Grid()
        grid.add(lblNome)
        grid.add(txtNome)
        grid.add(lblApelido)
        grid.add(txtApelido)
        grid.attach_next_to(lblTratamento,lblNome,Gtk.PositionType.BOTTOM,1,1)
        grid.attach_next_to(txtTratamento,lblTratamento,Gtk.PositionType.RIGHT,1,1)
        grid.attach_next_to(lblNomeUsuario,lblApelido,Gtk.PositionType.BOTTOM,1,1)
        grid.attach_next_to(txtNomeUsuario,lblNomeUsuario,Gtk.PositionType.RIGHT,1,1)
        grid.attach_next_to(lblFormato, lblTratamento, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(cmbFormato, lblFormato, Gtk.PositionType.RIGHT, 3, 1)

        #Combo Box (3)
        modelo = Gtk.ListStore(str)
        modelo.append(["pdf"])
        modelo.append(["docx"])
        modelo.append(["odt"])
        modelo.append(["texto"])

        cmbFormato.set_model(modelo)
        cmbFormato.set_entry_text_column(0)
        caixaV.pack_start(grid, False, False, 0)
        builder = Gtk.Builder()
        builder.add_from_file("./cadroCorreoGlade.glade")
        caixaH2 = builder.get_object("box1")
        caixaV.pack_start(caixaH2, False, False,0)

        #implementar el boton Cancelar para que cierre la ventana(4)

        caixaH3= Gtk.Box (orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        self.btnAceptar=Gtk.Button("Aceptar")
        self.btnAceptar.connect("clicked",self.on_btnAceptar_clicked)
        self.btnCancelar= Gtk.Button("Cancelar")
        self.btnCancelar.connect("clicked", self.on_btnCancelar_clicked)
        caixaH3.pack_end(self.btnAceptar, False, False, 0)
        caixaH3.pack_end(self.btnCancelar,False, False,0)
        caixaV.pack_start(caixaH3, True, False, 0)
        self.txtCorreo = builder.get_object("txtDireccionCorreo")
        self.txvListaCorreos = builder.get_object("txvListaCorreos")
        self.textbuffer = self.txvListaCorreos.get_buffer()
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()


    def on_btnCancelar_clicked(self, control):
        exit()

        #implementar el boton añadir (realizado con el boton aceptar)
    def on_btnAceptar_clicked(self,control):
        correo = self.txtCorreo.get_text()
        fin = self.textbuffer.get_end_iter()
        self.textbuffer.insert(fin, correo + "\n")


if __name__=="__main__":
    Exame()
    Gtk.main()