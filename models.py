from __init__ import db

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(100))
    password = db.Column(db.String(50))
    
    #Aqui em baixo ficará apenas as relações de chaves estrangeiras para melhor leitura.
    
    comentario = db.relationship('Comentario', back_populates="user")
    post = db.relationship('Post', back_populates ="user")
    
    def __repr__(self):
        return f"{self.id,self.nome,self.email, self.password}"

class Categoria(db.Model):
    __tablename__ = "categoria"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    nome = db.Column(db.String(50))
    descricao = db.Column(db.String(1024))
    
    #Aqui em baixo ficará apenas as relações de chaves estrangeiras para melhor leitura.
    
    post = db.relationship('Post', back_populates="categoria")
    postcategoria = db.relationship("PostCategoria", back_populates="categoria")
    
    def __repr__(self):
        return f"{self.id,self.nome,self.descricao}"

class Tag(db.Model):
    __tablename__ = "tag"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    nome = db.Column(db.String(50))
    
    #Aqui em baixo ficará apenas as relações de chaves estrangeiras para melhor leitura.
    
    post = db.relationship('Post', back_populates="tag")
    
    
class Comentario(db.Model):
    __tablename__ = "comentario"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    conteudo = db.Column(db.String(1024))
    data = db.Column(db.String(50))
    
    #Aqui em baixo ficará apenas as relações de chaves estrangeiras para melhor leitura.
    
    user = db.relationship('User', back_populates='comentario')
    postcomentario = db.relationship('PostComentario', back_populates='comentario')

class Post(db.Model):
    __tablename__ = "post"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    categoria_id = db.Column(db.Integer, db.ForeignKey("categoria.id"))
    tag_id = db.Column(db.Integer, db.ForeignKey("tag.id"))
    titulo_post = db.Column(db.String(120))
    conteudo = db.Column(db.String)
    imagem = db.Column(db.LargeBinary)
    data = db.Column(db.String(50))
    tipopostagem_id = db.Column(db.Integer, db.ForeignKey("tipopostagem.id"))
    
    #Aqui em baixo ficará apenas as relações de chaves estrangeiras para melhor leitura.
    
    user = db.relationship('User', back_populates = "post")
    categoria = db.relationship('Categoria', back_populates = "post")
    tag = db.relationship('Tag', back_populates ="post")
    postcomentario = db.relationship('PostComentario', back_populates='post')
    tipopostagem = db.relationship('TipoPostagem', back_populates="post")
    postcategoria = db.relationship("PostCategoria", back_populates="post")
    
    
class PostComentario(db.Model):
     __tablename__ = "postcomentario"  
     id = db.Column(db.Integer, primary_key=True, unique=True)
     post_id = db.Column(db.Integer, db.ForeignKey("post.id"))
     comentario_id = db.Column(db.Integer, db.ForeignKey("comentario.id"))
     
     #Aqui em baixo ficará apenas as relações de chaves estrangeiras para melhor leitura.
     
     post = db.relationship('Post', back_populates="postcomentario")
     comentario = db.relationship('Comentario', back_populates = "postcomentario")

class TipoPostagem(db.Model):
    __tablename__ ="tipopostagem"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    nome = db.Column(db.String(30))
    
    #Aqui em baixo ficará apenas as relações de chaves estrangeiras para melhor leitura.
    
    post = db.relationship('Post', back_populates="tipopostagem")
    

class PostCategoria(db.Model):
    __tablename__ = "postcategoria"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    categoria_id = db.Column(db.Integer, db.ForeignKey("categoria.id"))
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"))
    
    #Aqui em baixo ficará apenas as relações de chaves estrangeiras para melhor leitura.
    
    categoria = db.relationship("Categoria", back_populates="postcategoria")
    post = db.relationship("Post", back_populates="postcategoria")