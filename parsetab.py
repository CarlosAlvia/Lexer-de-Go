
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASSIGN BOOL BOOL_TYPE BREAK CASE CHAN COMMA COMMENT COMPLEX64 COMPLEX64_TYPE CONST CONTINUE DEFAULT DEFER DIVIDE DOSPUNTOS ELSE EQUAL FALLTHROUGH FLOAT64 FLOAT64_TYPE FMT FOR FUNC GO GOTO GREATER_EQUAL GREATER_THAN ID IF ILLEGAL IMPORT INT INTERFACE INT_TYPE LBRACE LBRACKET LESS_EQUAL LESS_THAN LPAREN MAP MINUS MOD NOT NOT_EQUAL OR PACKAGE PLUS POINTER PRINT_LN PUNTO RANGE RBRACE RBRACKET RETURN RPAREN SCANLN SELECT SEMICOLON STRING STRING_TYPE STRUCT SWITCH TIMES TYPE VARcodigo : asignacion\n              | sentenciaSwitch\n              | funcion\n              | funcionAnonima\n              | imprimir\n              | solicitudDatos\n              funcion : FUNC ID LPAREN argumentos RPAREN LBRACE subcodigo RBRACEargumentos : argumento\n                  | argumentoVariadico\n                  | argumento COMMA\n                  | argumentoVariadico COMMAargumento : ID tipoDato argumentoVariadico : ID PUNTO PUNTO PUNTO tipoDato funcionAnonima : FUNC LPAREN RPAREN LBRACE subcodigo RBRACE LPAREN RPARENfuncionAnonima : FUNC LPAREN argumentos RPAREN LBRACE subcodigo RBRACE LPAREN RPARENsubcodigo : asignacionCorta\n                  | asignacionsentenciaSwitch : SWITCH ID LBRACE bloqueCasosSwitch casoDefault RBRACEsentenciaSwitch : SWITCH asignacionCorta SEMICOLON ID LBRACE bloqueCasosSwitch casoDefault RBRACEsentenciaSwitch : SWITCH LBRACE bloqueCasosBooleanos casoDefault RBRACEbloqueCasosBooleanos : casoBooleano\n                            | casoBooleano bloqueCasosBooleanoscasoBooleano : CASE condiciones DOSPUNTOS subcodigo\n                      | CASE ID DOSPUNTOS subcodigocasoDefault : DEFAULT DOSPUNTOS subcodigo\n                   | emptybloqueCasosSwitch : casoSwitch\n                         | casoSwitch bloqueCasosSwitchcasoSwitch : CASE valores DOSPUNTOS subcodigoestructurasDeDatos : mapamapa : MAP LBRACKET tipoDato RBRACKET tipoDato LBRACE RBRACEmapa : MAP LBRACKET tipoDato RBRACKET tipoDato LBRACE elementosMapa RBRACEelementosMapa : elementoMapa\n                     | elementoMapa elementosMapaelementoMapa : valor DOSPUNTOS valor COMMAasignacion : VAR ID tipoDato EQUAL valorasignacion : VAR ID EQUAL valorasignacionCorta : ID DOSPUNTOS EQUAL valortipoDato : FLOAT64_TYPE\n                  | COMPLEX64_TYPE\n                  | INT_TYPE\n                  | BOOL_TYPE\n                  | STRING_TYPEvalores : valor\n               | valor COMMA valoresvalor : FLOAT64\n             | COMPLEX64\n             | INT\n             | BOOL\n             | STRING\n             | expresionesAritmeticas\n             | condiciones\n             | ID\n             | estructurasDeDatosexpresionesAritmeticas : expresionAritmetica\n                              | expresionAritmetica operador expresionesAritmeticasexpresionAritmetica : valor operador valor\n                             | LPAREN valor operador valor RPARENoperador : PLUS\n                | MINUS\n                | TIMES\n                | DIVIDE\n                | MODcondiciones : condicion\n                   | condicion conector condicionesconector : AND\n                | ORcondicion : valor operadorComp valor\n                 | BOOLoperadorComp : NOT_EQUAL\n                    | LESS_THAN\n                    | LESS_EQUAL\n                    | GREATER_THAN\n                    | GREATER_EQUALempty :imprimir : FMT PUNTO PRINT_LN LPAREN valores RPAREN\n                | FMT PUNTO PRINT_LN LPAREN RPARENsolicitudDatos : FMT PUNTO SCANLN LPAREN POINTER ID RPAREN'
    
_lr_action_items = {'VAR':([0,70,103,104,105,112,125,131,],[8,8,8,8,8,8,8,8,]),'SWITCH':([0,],[9,]),'FUNC':([0,],[10,]),'FMT':([0,],[11,]),'$end':([1,2,3,4,5,6,7,41,42,43,44,45,46,47,48,49,50,51,52,53,67,78,102,115,117,118,119,121,124,135,146,147,149,150,151,154,155,159,],[0,-1,-2,-3,-4,-5,-6,-53,-37,-46,-47,-48,-49,-50,-51,-52,-54,-55,-64,-30,-69,-36,-20,-77,-57,-68,-56,-65,-18,-76,-78,-58,-19,-7,-14,-15,-31,-32,]),'ID':([8,9,10,17,20,30,31,32,40,54,58,59,70,76,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,103,104,105,112,116,122,125,126,131,153,157,161,163,],[12,13,16,37,41,65,68,37,41,41,41,41,111,41,41,41,-59,-60,-61,-62,-63,-70,-71,-72,-73,-74,41,41,-66,-67,111,111,111,111,136,41,111,41,111,41,41,41,-35,]),'LBRACE':([9,13,21,22,23,24,25,33,68,71,107,148,],[14,26,-39,-40,-41,-42,-43,70,106,112,131,153,]),'LPAREN':([10,16,20,30,38,39,40,54,58,59,76,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,122,126,132,144,153,157,161,163,],[17,32,54,54,76,77,54,54,54,54,54,54,54,-59,-60,-61,-62,-63,-70,-71,-72,-73,-74,54,54,-66,-67,54,54,143,152,54,54,54,-35,]),'PUNTO':([11,37,75,113,],[18,75,113,134,]),'EQUAL':([12,19,21,22,23,24,25,27,],[20,40,-39,-40,-41,-42,-43,59,]),'FLOAT64_TYPE':([12,37,96,134,138,],[21,21,21,21,21,]),'COMPLEX64_TYPE':([12,37,96,134,138,],[22,22,22,22,22,]),'INT_TYPE':([12,37,96,134,138,],[23,23,23,23,23,]),'BOOL_TYPE':([12,37,96,134,138,],[24,24,24,24,24,]),'STRING_TYPE':([12,37,96,134,138,],[25,25,25,25,25,]),'DOSPUNTOS':([13,41,43,44,45,46,47,48,49,50,51,52,53,61,64,65,67,99,100,111,117,118,119,121,140,147,155,158,159,],[27,-53,-46,-47,-48,-49,-50,-51,-52,-54,-55,-64,-30,103,104,105,-69,125,-44,27,-57,-68,-56,-65,-45,-58,-31,161,-32,]),'CASE':([14,26,29,41,42,43,44,45,46,47,48,49,50,51,52,53,57,67,78,101,106,109,110,117,118,119,121,128,129,139,147,155,159,],[30,58,30,-53,-37,-46,-47,-48,-49,-50,-51,-52,-54,-55,-64,-30,58,-69,-36,-38,58,-16,-17,-57,-68,-56,-65,-23,-24,-29,-58,-31,-32,]),'SEMICOLON':([15,41,43,44,45,46,47,48,49,50,51,52,53,67,101,117,118,119,121,147,155,159,],[31,-53,-46,-47,-48,-49,-50,-51,-52,-54,-55,-64,-30,-69,-38,-57,-68,-56,-65,-58,-31,-32,]),'RPAREN':([17,21,22,23,24,25,34,35,36,41,43,44,45,46,47,48,49,50,51,52,53,67,69,72,73,74,76,100,114,117,118,119,121,136,137,140,143,145,147,152,155,159,],[33,-39,-40,-41,-42,-43,71,-8,-9,-53,-46,-47,-48,-49,-50,-51,-52,-54,-55,-64,-30,-69,107,-10,-11,-12,115,-44,135,-57,-68,-56,-65,146,147,-45,151,-13,-58,154,-31,-32,]),'PRINT_LN':([18,],[38,]),'SCANLN':([18,],[39,]),'FLOAT64':([20,30,40,54,58,59,76,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,122,126,153,157,161,163,],[43,43,43,43,43,43,43,43,43,-59,-60,-61,-62,-63,-70,-71,-72,-73,-74,43,43,-66,-67,43,43,43,43,43,-35,]),'COMPLEX64':([20,30,40,54,58,59,76,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,122,126,153,157,161,163,],[44,44,44,44,44,44,44,44,44,-59,-60,-61,-62,-63,-70,-71,-72,-73,-74,44,44,-66,-67,44,44,44,44,44,-35,]),'INT':([20,30,40,54,58,59,76,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,122,126,153,157,161,163,],[45,45,45,45,45,45,45,45,45,-59,-60,-61,-62,-63,-70,-71,-72,-73,-74,45,45,-66,-67,45,45,45,45,45,-35,]),'BOOL':([20,30,40,54,58,59,76,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,122,126,153,157,161,163,],[46,67,46,46,46,46,46,46,46,-59,-60,-61,-62,-63,-70,-71,-72,-73,-74,46,67,-66,-67,46,46,46,46,46,-35,]),'STRING':([20,30,40,54,58,59,76,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,122,126,153,157,161,163,],[47,47,47,47,47,47,47,47,47,-59,-60,-61,-62,-63,-70,-71,-72,-73,-74,47,47,-66,-67,47,47,47,47,47,-35,]),'MAP':([20,30,40,54,58,59,76,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,122,126,153,157,161,163,],[55,55,55,55,55,55,55,55,55,-59,-60,-61,-62,-63,-70,-71,-72,-73,-74,55,55,-66,-67,55,55,55,55,55,-35,]),'COMMA':([21,22,23,24,25,35,36,41,43,44,45,46,47,48,49,50,51,52,53,67,74,100,117,118,119,121,145,147,155,159,162,],[-39,-40,-41,-42,-43,72,73,-53,-46,-47,-48,-49,-50,-51,-52,-54,-55,-64,-30,-69,-12,126,-57,-68,-56,-65,-13,-58,-31,-32,163,]),'RBRACKET':([21,22,23,24,25,123,],[-39,-40,-41,-42,-43,138,]),'DEFAULT':([28,29,41,42,43,44,45,46,47,48,49,50,51,52,53,56,57,63,67,78,98,101,109,110,117,118,119,121,128,129,130,139,147,155,159,],[61,-21,-53,-37,-46,-47,-48,-49,-50,-51,-52,-54,-55,-64,-30,61,-27,-22,-69,-36,-28,-38,-16,-17,-57,-68,-56,-65,-23,-24,61,-29,-58,-31,-32,]),'RBRACE':([28,29,41,42,43,44,45,46,47,48,49,50,51,52,53,56,57,60,62,63,67,78,97,98,101,108,109,110,117,118,119,121,127,128,129,130,133,139,141,142,147,153,155,156,157,159,160,163,],[-75,-21,-53,-37,-46,-47,-48,-49,-50,-51,-52,-54,-55,-64,-30,-75,-27,102,-26,-22,-69,-36,124,-28,-38,132,-16,-17,-57,-68,-56,-65,-25,-23,-24,-75,144,-29,149,150,-58,155,-31,159,-33,-32,-34,-35,]),'PLUS':([41,42,43,44,45,46,47,48,49,50,51,52,53,64,65,66,67,78,95,100,101,117,118,119,120,121,137,147,155,158,159,162,],[-53,81,-46,-47,-48,-49,-50,-51,-52,-54,81,-64,-30,-52,-53,81,-49,81,81,81,81,81,81,-51,81,-52,81,-58,-31,81,-32,81,]),'MINUS':([41,42,43,44,45,46,47,48,49,50,51,52,53,64,65,66,67,78,95,100,101,117,118,119,120,121,137,147,155,158,159,162,],[-53,82,-46,-47,-48,-49,-50,-51,-52,-54,82,-64,-30,-52,-53,82,-49,82,82,82,82,82,82,-51,82,-52,82,-58,-31,82,-32,82,]),'TIMES':([41,42,43,44,45,46,47,48,49,50,51,52,53,64,65,66,67,78,95,100,101,117,118,119,120,121,137,147,155,158,159,162,],[-53,83,-46,-47,-48,-49,-50,-51,-52,-54,83,-64,-30,-52,-53,83,-49,83,83,83,83,83,83,-51,83,-52,83,-58,-31,83,-32,83,]),'DIVIDE':([41,42,43,44,45,46,47,48,49,50,51,52,53,64,65,66,67,78,95,100,101,117,118,119,120,121,137,147,155,158,159,162,],[-53,84,-46,-47,-48,-49,-50,-51,-52,-54,84,-64,-30,-52,-53,84,-49,84,84,84,84,84,84,-51,84,-52,84,-58,-31,84,-32,84,]),'MOD':([41,42,43,44,45,46,47,48,49,50,51,52,53,64,65,66,67,78,95,100,101,117,118,119,120,121,137,147,155,158,159,162,],[-53,85,-46,-47,-48,-49,-50,-51,-52,-54,85,-64,-30,-52,-53,85,-49,85,85,85,85,85,85,-51,85,-52,85,-58,-31,85,-32,85,]),'NOT_EQUAL':([41,42,43,44,45,46,47,48,49,50,51,52,53,64,65,66,67,78,95,100,101,117,118,119,120,121,137,147,155,158,159,162,],[-53,86,-46,-47,-48,-49,-50,-51,-52,-54,-55,-64,-30,-52,-53,86,-49,86,86,86,86,86,86,-51,86,-52,86,-58,-31,86,-32,86,]),'LESS_THAN':([41,42,43,44,45,46,47,48,49,50,51,52,53,64,65,66,67,78,95,100,101,117,118,119,120,121,137,147,155,158,159,162,],[-53,87,-46,-47,-48,-49,-50,-51,-52,-54,-55,-64,-30,-52,-53,87,-49,87,87,87,87,87,87,-51,87,-52,87,-58,-31,87,-32,87,]),'LESS_EQUAL':([41,42,43,44,45,46,47,48,49,50,51,52,53,64,65,66,67,78,95,100,101,117,118,119,120,121,137,147,155,158,159,162,],[-53,88,-46,-47,-48,-49,-50,-51,-52,-54,-55,-64,-30,-52,-53,88,-49,88,88,88,88,88,88,-51,88,-52,88,-58,-31,88,-32,88,]),'GREATER_THAN':([41,42,43,44,45,46,47,48,49,50,51,52,53,64,65,66,67,78,95,100,101,117,118,119,120,121,137,147,155,158,159,162,],[-53,89,-46,-47,-48,-49,-50,-51,-52,-54,-55,-64,-30,-52,-53,89,-49,89,89,89,89,89,89,-51,89,-52,89,-58,-31,89,-32,89,]),'GREATER_EQUAL':([41,42,43,44,45,46,47,48,49,50,51,52,53,64,65,66,67,78,95,100,101,117,118,119,120,121,137,147,155,158,159,162,],[-53,90,-46,-47,-48,-49,-50,-51,-52,-54,-55,-64,-30,-52,-53,90,-49,90,90,90,90,90,90,-51,90,-52,90,-58,-31,90,-32,90,]),'AND':([41,43,44,45,46,47,48,49,50,51,52,53,67,117,118,119,121,147,155,159,],[-53,-46,-47,-48,-49,-50,-51,-52,-54,-55,93,-30,-69,-57,-68,-56,-65,-58,-31,-32,]),'OR':([41,43,44,45,46,47,48,49,50,51,52,53,67,117,118,119,121,147,155,159,],[-53,-46,-47,-48,-49,-50,-51,-52,-54,-55,94,-30,-69,-57,-68,-56,-65,-58,-31,-32,]),'LBRACKET':([55,],[96,]),'POINTER':([77,],[116,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'codigo':([0,],[1,]),'asignacion':([0,70,103,104,105,112,125,131,],[2,110,110,110,110,110,110,110,]),'sentenciaSwitch':([0,],[3,]),'funcion':([0,],[4,]),'funcionAnonima':([0,],[5,]),'imprimir':([0,],[6,]),'solicitudDatos':([0,],[7,]),'asignacionCorta':([9,70,103,104,105,112,125,131,],[15,109,109,109,109,109,109,109,]),'tipoDato':([12,37,96,134,138,],[19,74,123,145,148,]),'bloqueCasosBooleanos':([14,29,],[28,63,]),'casoBooleano':([14,29,],[29,29,]),'argumentos':([17,32,],[34,69,]),'argumento':([17,32,],[35,35,]),'argumentoVariadico':([17,32,],[36,36,]),'valor':([20,30,40,54,58,59,76,79,80,91,92,122,126,153,157,161,],[42,66,78,95,100,101,100,117,118,120,66,137,100,158,158,162,]),'expresionesAritmeticas':([20,30,40,54,58,59,76,79,80,91,92,122,126,153,157,161,],[48,48,48,48,48,48,48,48,48,119,48,48,48,48,48,48,]),'condiciones':([20,30,40,54,58,59,76,79,80,91,92,122,126,153,157,161,],[49,64,49,49,49,49,49,49,49,49,121,49,49,49,49,49,]),'estructurasDeDatos':([20,30,40,54,58,59,76,79,80,91,92,122,126,153,157,161,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'expresionAritmetica':([20,30,40,54,58,59,76,79,80,91,92,122,126,153,157,161,],[51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,]),'condicion':([20,30,40,54,58,59,76,79,80,91,92,122,126,153,157,161,],[52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,]),'mapa':([20,30,40,54,58,59,76,79,80,91,92,122,126,153,157,161,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'bloqueCasosSwitch':([26,57,106,],[56,98,130,]),'casoSwitch':([26,57,106,],[57,57,57,]),'casoDefault':([28,56,130,],[60,97,141,]),'empty':([28,56,130,],[62,62,62,]),'operador':([42,51,66,78,95,100,101,117,118,120,137,158,162,],[79,91,79,79,122,79,79,79,79,79,79,79,79,]),'operadorComp':([42,66,78,95,100,101,117,118,120,137,158,162,],[80,80,80,80,80,80,80,80,80,80,80,80,]),'conector':([52,],[92,]),'valores':([58,76,126,],[99,114,140,]),'subcodigo':([70,103,104,105,112,125,131,],[108,127,128,129,133,139,142,]),'elementosMapa':([153,157,],[156,160,]),'elementoMapa':([153,157,],[157,157,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> codigo","S'",1,None,None,None),
  ('codigo -> asignacion','codigo',1,'p_codigo','parserGo.py',6),
  ('codigo -> sentenciaSwitch','codigo',1,'p_codigo','parserGo.py',7),
  ('codigo -> funcion','codigo',1,'p_codigo','parserGo.py',8),
  ('codigo -> funcionAnonima','codigo',1,'p_codigo','parserGo.py',9),
  ('codigo -> imprimir','codigo',1,'p_codigo','parserGo.py',10),
  ('codigo -> solicitudDatos','codigo',1,'p_codigo','parserGo.py',11),
  ('funcion -> FUNC ID LPAREN argumentos RPAREN LBRACE subcodigo RBRACE','funcion',8,'p_funcion','parserGo.py',16),
  ('argumentos -> argumento','argumentos',1,'p_argumentos','parserGo.py',19),
  ('argumentos -> argumentoVariadico','argumentos',1,'p_argumentos','parserGo.py',20),
  ('argumentos -> argumento COMMA','argumentos',2,'p_argumentos','parserGo.py',21),
  ('argumentos -> argumentoVariadico COMMA','argumentos',2,'p_argumentos','parserGo.py',22),
  ('argumento -> ID tipoDato','argumento',2,'p_argumento','parserGo.py',25),
  ('argumentoVariadico -> ID PUNTO PUNTO PUNTO tipoDato','argumentoVariadico',5,'p_argumentoVariadico','parserGo.py',28),
  ('funcionAnonima -> FUNC LPAREN RPAREN LBRACE subcodigo RBRACE LPAREN RPAREN','funcionAnonima',8,'p_funcion_anonima','parserGo.py',31),
  ('funcionAnonima -> FUNC LPAREN argumentos RPAREN LBRACE subcodigo RBRACE LPAREN RPAREN','funcionAnonima',9,'p_funcion_anonima_variadico','parserGo.py',34),
  ('subcodigo -> asignacionCorta','subcodigo',1,'p_subcodigo','parserGo.py',38),
  ('subcodigo -> asignacion','subcodigo',1,'p_subcodigo','parserGo.py',39),
  ('sentenciaSwitch -> SWITCH ID LBRACE bloqueCasosSwitch casoDefault RBRACE','sentenciaSwitch',6,'p_sentenciaSwitchClasica','parserGo.py',42),
  ('sentenciaSwitch -> SWITCH asignacionCorta SEMICOLON ID LBRACE bloqueCasosSwitch casoDefault RBRACE','sentenciaSwitch',8,'p_switchConDefinicionDeVariable','parserGo.py',45),
  ('sentenciaSwitch -> SWITCH LBRACE bloqueCasosBooleanos casoDefault RBRACE','sentenciaSwitch',5,'p_switchNoCondicion','parserGo.py',48),
  ('bloqueCasosBooleanos -> casoBooleano','bloqueCasosBooleanos',1,'p_bloqueCasosBooleanos','parserGo.py',51),
  ('bloqueCasosBooleanos -> casoBooleano bloqueCasosBooleanos','bloqueCasosBooleanos',2,'p_bloqueCasosBooleanos','parserGo.py',52),
  ('casoBooleano -> CASE condiciones DOSPUNTOS subcodigo','casoBooleano',4,'p_casoBooleano','parserGo.py',55),
  ('casoBooleano -> CASE ID DOSPUNTOS subcodigo','casoBooleano',4,'p_casoBooleano','parserGo.py',56),
  ('casoDefault -> DEFAULT DOSPUNTOS subcodigo','casoDefault',3,'p_casoDefault','parserGo.py',59),
  ('casoDefault -> empty','casoDefault',1,'p_casoDefault','parserGo.py',60),
  ('bloqueCasosSwitch -> casoSwitch','bloqueCasosSwitch',1,'p_bloqueCasosSwitch','parserGo.py',63),
  ('bloqueCasosSwitch -> casoSwitch bloqueCasosSwitch','bloqueCasosSwitch',2,'p_bloqueCasosSwitch','parserGo.py',64),
  ('casoSwitch -> CASE valores DOSPUNTOS subcodigo','casoSwitch',4,'p_casoSwitch','parserGo.py',67),
  ('estructurasDeDatos -> mapa','estructurasDeDatos',1,'p_estructurasDeDatos','parserGo.py',72),
  ('mapa -> MAP LBRACKET tipoDato RBRACKET tipoDato LBRACE RBRACE','mapa',7,'p_definicionMapaVacio','parserGo.py',75),
  ('mapa -> MAP LBRACKET tipoDato RBRACKET tipoDato LBRACE elementosMapa RBRACE','mapa',8,'p_definicionMapaValores','parserGo.py',78),
  ('elementosMapa -> elementoMapa','elementosMapa',1,'p_elementosMapa','parserGo.py',81),
  ('elementosMapa -> elementoMapa elementosMapa','elementosMapa',2,'p_elementosMapa','parserGo.py',82),
  ('elementoMapa -> valor DOSPUNTOS valor COMMA','elementoMapa',4,'p_elementoMapa','parserGo.py',85),
  ('asignacion -> VAR ID tipoDato EQUAL valor','asignacion',5,'p_asignacionTipo','parserGo.py',89),
  ('asignacion -> VAR ID EQUAL valor','asignacion',4,'p_asignacionInferencia','parserGo.py',92),
  ('asignacionCorta -> ID DOSPUNTOS EQUAL valor','asignacionCorta',4,'p_asignacionCorta','parserGo.py',95),
  ('tipoDato -> FLOAT64_TYPE','tipoDato',1,'p_tipoDato','parserGo.py',98),
  ('tipoDato -> COMPLEX64_TYPE','tipoDato',1,'p_tipoDato','parserGo.py',99),
  ('tipoDato -> INT_TYPE','tipoDato',1,'p_tipoDato','parserGo.py',100),
  ('tipoDato -> BOOL_TYPE','tipoDato',1,'p_tipoDato','parserGo.py',101),
  ('tipoDato -> STRING_TYPE','tipoDato',1,'p_tipoDato','parserGo.py',102),
  ('valores -> valor','valores',1,'p_valores','parserGo.py',105),
  ('valores -> valor COMMA valores','valores',3,'p_valores','parserGo.py',106),
  ('valor -> FLOAT64','valor',1,'p_valor','parserGo.py',109),
  ('valor -> COMPLEX64','valor',1,'p_valor','parserGo.py',110),
  ('valor -> INT','valor',1,'p_valor','parserGo.py',111),
  ('valor -> BOOL','valor',1,'p_valor','parserGo.py',112),
  ('valor -> STRING','valor',1,'p_valor','parserGo.py',113),
  ('valor -> expresionesAritmeticas','valor',1,'p_valor','parserGo.py',114),
  ('valor -> condiciones','valor',1,'p_valor','parserGo.py',115),
  ('valor -> ID','valor',1,'p_valor','parserGo.py',116),
  ('valor -> estructurasDeDatos','valor',1,'p_valor','parserGo.py',117),
  ('expresionesAritmeticas -> expresionAritmetica','expresionesAritmeticas',1,'p_expresionesAritmeticas','parserGo.py',121),
  ('expresionesAritmeticas -> expresionAritmetica operador expresionesAritmeticas','expresionesAritmeticas',3,'p_expresionesAritmeticas','parserGo.py',122),
  ('expresionAritmetica -> valor operador valor','expresionAritmetica',3,'p_expresionAritmetica','parserGo.py',125),
  ('expresionAritmetica -> LPAREN valor operador valor RPAREN','expresionAritmetica',5,'p_expresionAritmetica','parserGo.py',126),
  ('operador -> PLUS','operador',1,'p_operador','parserGo.py',129),
  ('operador -> MINUS','operador',1,'p_operador','parserGo.py',130),
  ('operador -> TIMES','operador',1,'p_operador','parserGo.py',131),
  ('operador -> DIVIDE','operador',1,'p_operador','parserGo.py',132),
  ('operador -> MOD','operador',1,'p_operador','parserGo.py',133),
  ('condiciones -> condicion','condiciones',1,'p_condiciones','parserGo.py',137),
  ('condiciones -> condicion conector condiciones','condiciones',3,'p_condiciones','parserGo.py',138),
  ('conector -> AND','conector',1,'p_conector','parserGo.py',141),
  ('conector -> OR','conector',1,'p_conector','parserGo.py',142),
  ('condicion -> valor operadorComp valor','condicion',3,'p_condicion','parserGo.py',145),
  ('condicion -> BOOL','condicion',1,'p_condicion','parserGo.py',146),
  ('operadorComp -> NOT_EQUAL','operadorComp',1,'p_operadorComparacion','parserGo.py',149),
  ('operadorComp -> LESS_THAN','operadorComp',1,'p_operadorComparacion','parserGo.py',150),
  ('operadorComp -> LESS_EQUAL','operadorComp',1,'p_operadorComparacion','parserGo.py',151),
  ('operadorComp -> GREATER_THAN','operadorComp',1,'p_operadorComparacion','parserGo.py',152),
  ('operadorComp -> GREATER_EQUAL','operadorComp',1,'p_operadorComparacion','parserGo.py',153),
  ('empty -> <empty>','empty',0,'p_empty','parserGo.py',156),
  ('imprimir -> FMT PUNTO PRINT_LN LPAREN valores RPAREN','imprimir',6,'p_imprimir','parserGo.py',161),
  ('imprimir -> FMT PUNTO PRINT_LN LPAREN RPAREN','imprimir',5,'p_imprimir','parserGo.py',162),
  ('solicitudDatos -> FMT PUNTO SCANLN LPAREN POINTER ID RPAREN','solicitudDatos',7,'p_solicitud_datos','parserGo.py',165),
]
