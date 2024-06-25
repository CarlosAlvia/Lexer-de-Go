
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASSIGN BOOL BOOL_TYPE BREAK CASE CHAN COMMA COMMENT COMPLEX64 COMPLEX64_TYPE CONST CONTINUE DEFAULT DEFER DIVIDE DOSPUNTOS ELSE EQUAL FALLTHROUGH FLOAT64 FLOAT64_TYPE FMT FOR FUNC GO GOTO GREATER_EQUAL GREATER_THAN ID IF ILLEGAL IMPORT INT INTERFACE INT_TYPE LBRACE LBRACKET LESS_EQUAL LESS_THAN LPAREN MAP MINUS MOD NOT NOT_EQUAL OR PACKAGE PLUS PRINT_LN PUNTO RANGE RBRACE RBRACKET RETURN RPAREN SELECT SEMICOLON STRING STRING_TYPE STRUCT SWITCH TIMES TYPE VARcodigo : asignacion\n              | sentenciaSwitch\n              | funcion\n              | imprimirfuncion : FUNC ID LPAREN argumentos RPAREN LBRACE subcodigo RBRACEargumentos : argumento\n                  | argumentoVariadico\n                  | argumento COMMA\n                  | argumentoVariadico COMMAargumento : ID tipoDato argumentoVariadico : ID PUNTO PUNTO PUNTO tipoDato subcodigo : asignacionCorta\n                  | asignacionsentenciaSwitch : SWITCH ID LBRACE bloqueCasosSwitch casoDefault RBRACEsentenciaSwitch : SWITCH asignacionCorta SEMICOLON ID LBRACE bloqueCasosSwitch casoDefault RBRACEsentenciaSwitch : SWITCH LBRACE bloqueCasosBooleanos casoDefault RBRACEbloqueCasosBooleanos : casoBooleano\n                            | casoBooleano bloqueCasosBooleanoscasoBooleano : CASE condiciones DOSPUNTOS subcodigo\n                      | CASE ID DOSPUNTOS subcodigocasoDefault : DEFAULT DOSPUNTOS subcodigo\n                   | emptybloqueCasosSwitch : casoSwitch\n                         | casoSwitch bloqueCasosSwitchcasoSwitch : CASE valores DOSPUNTOS subcodigoestructurasDeDatos : mapamapa : MAP LBRACKET tipoDato RBRACKET tipoDato LBRACE RBRACEmapa : MAP LBRACKET tipoDato RBRACKET tipoDato LBRACE elementosMapa RBRACEelementosMapa : elementoMapa\n                     | elementoMapa elementosMapaelementoMapa : valor DOSPUNTOS valor COMMAasignacion : VAR ID tipoDato EQUAL valorasignacion : VAR ID EQUAL valorasignacionCorta : ID DOSPUNTOS EQUAL valortipoDato : FLOAT64_TYPE\n                  | COMPLEX64_TYPE\n                  | INT_TYPE\n                  | BOOL_TYPE\n                  | STRING_TYPEvalores : valor\n               | valor COMMA valoresvalor : FLOAT64\n             | COMPLEX64\n             | INT\n             | BOOL\n             | STRING\n             | expresionesAritmeticas\n             | condiciones\n             | ID\n             | estructurasDeDatosexpresionesAritmeticas : expresionAritmetica\n                              | expresionAritmetica operador expresionesAritmeticasexpresionAritmetica : valor operador valor\n                             | LPAREN valor operador valor RPARENoperador : PLUS\n                | MINUS\n                | TIMES\n                | DIVIDE\n                | MODcondiciones : condicion\n                   | condicion conector condicionesconector : AND\n                | ORcondicion : valor operadorComp valor\n                 | BOOLoperadorComp : NOT_EQUAL\n                    | LESS_THAN\n                    | LESS_EQUAL\n                    | GREATER_THAN\n                    | GREATER_EQUALempty :imprimir : FMT PUNTO PRINT_LN LPAREN valores RPAREN\n                | FMT PUNTO PRINT_LN LPAREN RPAREN'
    
_lr_action_items = {'VAR':([0,90,91,92,109,119,],[6,6,6,6,6,6,]),'SWITCH':([0,],[7,]),'FUNC':([0,],[8,]),'FMT':([0,],[9,]),'$end':([1,2,3,4,5,32,33,34,35,36,37,38,39,40,41,42,43,44,58,65,89,100,101,102,103,105,108,120,128,130,132,134,138,],[0,-1,-2,-3,-4,-49,-33,-42,-43,-44,-45,-46,-47,-48,-50,-51,-60,-26,-65,-32,-16,-73,-53,-64,-52,-61,-14,-72,-54,-15,-5,-27,-28,]),'ID':([6,7,8,17,27,28,29,31,45,49,50,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,90,91,92,106,109,110,119,133,136,140,142,],[10,11,14,32,56,59,60,32,32,32,32,32,32,32,-55,-56,-57,-58,-59,-66,-67,-68,-69,-70,32,32,-62,-63,114,114,114,32,114,32,114,32,32,32,-31,]),'LBRACE':([7,11,18,19,20,21,22,59,96,129,],[12,23,-35,-36,-37,-38,-39,93,119,133,]),'PUNTO':([9,60,95,118,],[15,95,118,126,]),'EQUAL':([10,16,18,19,20,21,22,24,],[17,31,-35,-36,-37,-38,-39,50,]),'FLOAT64_TYPE':([10,60,83,122,126,],[18,18,18,18,18,]),'COMPLEX64_TYPE':([10,60,83,122,126,],[19,19,19,19,19,]),'INT_TYPE':([10,60,83,122,126,],[20,20,20,20,20,]),'BOOL_TYPE':([10,60,83,122,126,],[21,21,21,21,21,]),'STRING_TYPE':([10,60,83,122,126,],[22,22,22,22,22,]),'DOSPUNTOS':([11,32,34,35,36,37,38,39,40,41,42,43,44,52,55,56,58,86,87,101,102,103,105,114,124,128,134,137,138,],[24,-49,-42,-43,-44,-45,-46,-47,-48,-50,-51,-60,-26,90,91,92,-65,109,-40,-53,-64,-52,-61,24,-41,-54,-27,140,-28,]),'CASE':([12,23,26,32,33,34,35,36,37,38,39,40,41,42,43,44,48,58,65,88,93,101,102,103,105,112,113,115,116,123,128,134,138,],[27,49,27,-49,-33,-42,-43,-44,-45,-46,-47,-48,-50,-51,-60,-26,49,-65,-32,-34,49,-53,-64,-52,-61,-12,-13,-19,-20,-25,-54,-27,-28,]),'SEMICOLON':([13,32,34,35,36,37,38,39,40,41,42,43,44,58,88,101,102,103,105,128,134,138,],[28,-49,-42,-43,-44,-45,-46,-47,-48,-50,-51,-60,-26,-65,-34,-53,-64,-52,-61,-54,-27,-28,]),'LPAREN':([14,17,27,30,31,45,49,50,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,106,110,133,136,140,142,],[29,45,45,64,45,45,45,45,45,45,45,-55,-56,-57,-58,-59,-66,-67,-68,-69,-70,45,45,-62,-63,45,45,45,45,45,-31,]),'PRINT_LN':([15,],[30,]),'FLOAT64':([17,27,31,45,49,50,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,106,110,133,136,140,142,],[34,34,34,34,34,34,34,34,34,-55,-56,-57,-58,-59,-66,-67,-68,-69,-70,34,34,-62,-63,34,34,34,34,34,-31,]),'COMPLEX64':([17,27,31,45,49,50,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,106,110,133,136,140,142,],[35,35,35,35,35,35,35,35,35,-55,-56,-57,-58,-59,-66,-67,-68,-69,-70,35,35,-62,-63,35,35,35,35,35,-31,]),'INT':([17,27,31,45,49,50,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,106,110,133,136,140,142,],[36,36,36,36,36,36,36,36,36,-55,-56,-57,-58,-59,-66,-67,-68,-69,-70,36,36,-62,-63,36,36,36,36,36,-31,]),'BOOL':([17,27,31,45,49,50,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,106,110,133,136,140,142,],[37,58,37,37,37,37,37,37,37,-55,-56,-57,-58,-59,-66,-67,-68,-69,-70,37,58,-62,-63,37,37,37,37,37,-31,]),'STRING':([17,27,31,45,49,50,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,106,110,133,136,140,142,],[38,38,38,38,38,38,38,38,38,-55,-56,-57,-58,-59,-66,-67,-68,-69,-70,38,38,-62,-63,38,38,38,38,38,-31,]),'MAP':([17,27,31,45,49,50,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,106,110,133,136,140,142,],[46,46,46,46,46,46,46,46,46,-55,-56,-57,-58,-59,-66,-67,-68,-69,-70,46,46,-62,-63,46,46,46,46,46,-31,]),'COMMA':([18,19,20,21,22,32,34,35,36,37,38,39,40,41,42,43,44,58,62,63,87,94,101,102,103,105,128,131,134,138,141,],[-35,-36,-37,-38,-39,-49,-42,-43,-44,-45,-46,-47,-48,-50,-51,-60,-26,-65,97,98,110,-10,-53,-64,-52,-61,-54,-11,-27,-28,142,]),'RPAREN':([18,19,20,21,22,32,34,35,36,37,38,39,40,41,42,43,44,58,61,62,63,64,87,94,97,98,99,101,102,103,105,121,124,128,131,134,138,],[-35,-36,-37,-38,-39,-49,-42,-43,-44,-45,-46,-47,-48,-50,-51,-60,-26,-65,96,-6,-7,100,-40,-10,-8,-9,120,-53,-64,-52,-61,128,-41,-54,-11,-27,-28,]),'RBRACKET':([18,19,20,21,22,107,],[-35,-36,-37,-38,-39,122,]),'DEFAULT':([25,26,32,33,34,35,36,37,38,39,40,41,42,43,44,47,48,54,58,65,85,88,101,102,103,105,112,113,115,116,117,123,128,134,138,],[52,-17,-49,-33,-42,-43,-44,-45,-46,-47,-48,-50,-51,-60,-26,52,-23,-18,-65,-32,-24,-34,-53,-64,-52,-61,-12,-13,-19,-20,52,-25,-54,-27,-28,]),'RBRACE':([25,26,32,33,34,35,36,37,38,39,40,41,42,43,44,47,48,51,53,54,58,65,84,85,88,101,102,103,105,111,112,113,115,116,117,123,125,127,128,133,134,135,136,138,139,142,],[-71,-17,-49,-33,-42,-43,-44,-45,-46,-47,-48,-50,-51,-60,-26,-71,-23,89,-22,-18,-65,-32,108,-24,-34,-53,-64,-52,-61,-21,-12,-13,-19,-20,-71,-25,130,132,-54,134,-27,138,-29,-28,-30,-31,]),'PLUS':([32,33,34,35,36,37,38,39,40,41,42,43,44,55,56,57,58,65,82,87,88,101,102,103,104,105,121,128,134,137,138,141,],[-49,68,-42,-43,-44,-45,-46,-47,-48,-50,68,-60,-26,-48,-49,68,-45,68,68,68,68,68,68,-47,68,-48,68,-54,-27,68,-28,68,]),'MINUS':([32,33,34,35,36,37,38,39,40,41,42,43,44,55,56,57,58,65,82,87,88,101,102,103,104,105,121,128,134,137,138,141,],[-49,69,-42,-43,-44,-45,-46,-47,-48,-50,69,-60,-26,-48,-49,69,-45,69,69,69,69,69,69,-47,69,-48,69,-54,-27,69,-28,69,]),'TIMES':([32,33,34,35,36,37,38,39,40,41,42,43,44,55,56,57,58,65,82,87,88,101,102,103,104,105,121,128,134,137,138,141,],[-49,70,-42,-43,-44,-45,-46,-47,-48,-50,70,-60,-26,-48,-49,70,-45,70,70,70,70,70,70,-47,70,-48,70,-54,-27,70,-28,70,]),'DIVIDE':([32,33,34,35,36,37,38,39,40,41,42,43,44,55,56,57,58,65,82,87,88,101,102,103,104,105,121,128,134,137,138,141,],[-49,71,-42,-43,-44,-45,-46,-47,-48,-50,71,-60,-26,-48,-49,71,-45,71,71,71,71,71,71,-47,71,-48,71,-54,-27,71,-28,71,]),'MOD':([32,33,34,35,36,37,38,39,40,41,42,43,44,55,56,57,58,65,82,87,88,101,102,103,104,105,121,128,134,137,138,141,],[-49,72,-42,-43,-44,-45,-46,-47,-48,-50,72,-60,-26,-48,-49,72,-45,72,72,72,72,72,72,-47,72,-48,72,-54,-27,72,-28,72,]),'NOT_EQUAL':([32,33,34,35,36,37,38,39,40,41,42,43,44,55,56,57,58,65,82,87,88,101,102,103,104,105,121,128,134,137,138,141,],[-49,73,-42,-43,-44,-45,-46,-47,-48,-50,-51,-60,-26,-48,-49,73,-45,73,73,73,73,73,73,-47,73,-48,73,-54,-27,73,-28,73,]),'LESS_THAN':([32,33,34,35,36,37,38,39,40,41,42,43,44,55,56,57,58,65,82,87,88,101,102,103,104,105,121,128,134,137,138,141,],[-49,74,-42,-43,-44,-45,-46,-47,-48,-50,-51,-60,-26,-48,-49,74,-45,74,74,74,74,74,74,-47,74,-48,74,-54,-27,74,-28,74,]),'LESS_EQUAL':([32,33,34,35,36,37,38,39,40,41,42,43,44,55,56,57,58,65,82,87,88,101,102,103,104,105,121,128,134,137,138,141,],[-49,75,-42,-43,-44,-45,-46,-47,-48,-50,-51,-60,-26,-48,-49,75,-45,75,75,75,75,75,75,-47,75,-48,75,-54,-27,75,-28,75,]),'GREATER_THAN':([32,33,34,35,36,37,38,39,40,41,42,43,44,55,56,57,58,65,82,87,88,101,102,103,104,105,121,128,134,137,138,141,],[-49,76,-42,-43,-44,-45,-46,-47,-48,-50,-51,-60,-26,-48,-49,76,-45,76,76,76,76,76,76,-47,76,-48,76,-54,-27,76,-28,76,]),'GREATER_EQUAL':([32,33,34,35,36,37,38,39,40,41,42,43,44,55,56,57,58,65,82,87,88,101,102,103,104,105,121,128,134,137,138,141,],[-49,77,-42,-43,-44,-45,-46,-47,-48,-50,-51,-60,-26,-48,-49,77,-45,77,77,77,77,77,77,-47,77,-48,77,-54,-27,77,-28,77,]),'AND':([32,34,35,36,37,38,39,40,41,42,43,44,58,101,102,103,105,128,134,138,],[-49,-42,-43,-44,-45,-46,-47,-48,-50,-51,80,-26,-65,-53,-64,-52,-61,-54,-27,-28,]),'OR':([32,34,35,36,37,38,39,40,41,42,43,44,58,101,102,103,105,128,134,138,],[-49,-42,-43,-44,-45,-46,-47,-48,-50,-51,81,-26,-65,-53,-64,-52,-61,-54,-27,-28,]),'LBRACKET':([46,],[83,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'codigo':([0,],[1,]),'asignacion':([0,90,91,92,109,119,],[2,113,113,113,113,113,]),'sentenciaSwitch':([0,],[3,]),'funcion':([0,],[4,]),'imprimir':([0,],[5,]),'asignacionCorta':([7,90,91,92,109,119,],[13,112,112,112,112,112,]),'tipoDato':([10,60,83,122,126,],[16,94,107,129,131,]),'bloqueCasosBooleanos':([12,26,],[25,54,]),'casoBooleano':([12,26,],[26,26,]),'valor':([17,27,31,45,49,50,64,66,67,78,79,106,110,133,136,140,],[33,57,65,82,87,88,87,101,102,104,57,121,87,137,137,141,]),'expresionesAritmeticas':([17,27,31,45,49,50,64,66,67,78,79,106,110,133,136,140,],[39,39,39,39,39,39,39,39,39,103,39,39,39,39,39,39,]),'condiciones':([17,27,31,45,49,50,64,66,67,78,79,106,110,133,136,140,],[40,55,40,40,40,40,40,40,40,40,105,40,40,40,40,40,]),'estructurasDeDatos':([17,27,31,45,49,50,64,66,67,78,79,106,110,133,136,140,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'expresionAritmetica':([17,27,31,45,49,50,64,66,67,78,79,106,110,133,136,140,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'condicion':([17,27,31,45,49,50,64,66,67,78,79,106,110,133,136,140,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'mapa':([17,27,31,45,49,50,64,66,67,78,79,106,110,133,136,140,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'bloqueCasosSwitch':([23,48,93,],[47,85,117,]),'casoSwitch':([23,48,93,],[48,48,48,]),'casoDefault':([25,47,117,],[51,84,125,]),'empty':([25,47,117,],[53,53,53,]),'argumentos':([29,],[61,]),'argumento':([29,],[62,]),'argumentoVariadico':([29,],[63,]),'operador':([33,42,57,65,82,87,88,101,102,104,121,137,141,],[66,78,66,66,106,66,66,66,66,66,66,66,66,]),'operadorComp':([33,57,65,82,87,88,101,102,104,121,137,141,],[67,67,67,67,67,67,67,67,67,67,67,67,]),'conector':([43,],[79,]),'valores':([49,64,110,],[86,99,124,]),'subcodigo':([90,91,92,109,119,],[111,115,116,123,127,]),'elementosMapa':([133,136,],[135,139,]),'elementoMapa':([133,136,],[136,136,]),}

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
  ('codigo -> imprimir','codigo',1,'p_codigo','parserGo.py',9),
  ('funcion -> FUNC ID LPAREN argumentos RPAREN LBRACE subcodigo RBRACE','funcion',8,'p_funcion','parserGo.py',13),
  ('argumentos -> argumento','argumentos',1,'p_argumentos','parserGo.py',16),
  ('argumentos -> argumentoVariadico','argumentos',1,'p_argumentos','parserGo.py',17),
  ('argumentos -> argumento COMMA','argumentos',2,'p_argumentos','parserGo.py',18),
  ('argumentos -> argumentoVariadico COMMA','argumentos',2,'p_argumentos','parserGo.py',19),
  ('argumento -> ID tipoDato','argumento',2,'p_argumento','parserGo.py',22),
  ('argumentoVariadico -> ID PUNTO PUNTO PUNTO tipoDato','argumentoVariadico',5,'p_argumentoVariadico','parserGo.py',25),
  ('subcodigo -> asignacionCorta','subcodigo',1,'p_subcodigo','parserGo.py',29),
  ('subcodigo -> asignacion','subcodigo',1,'p_subcodigo','parserGo.py',30),
  ('sentenciaSwitch -> SWITCH ID LBRACE bloqueCasosSwitch casoDefault RBRACE','sentenciaSwitch',6,'p_sentenciaSwitchClasica','parserGo.py',33),
  ('sentenciaSwitch -> SWITCH asignacionCorta SEMICOLON ID LBRACE bloqueCasosSwitch casoDefault RBRACE','sentenciaSwitch',8,'p_switchConDefinicionDeVariable','parserGo.py',36),
  ('sentenciaSwitch -> SWITCH LBRACE bloqueCasosBooleanos casoDefault RBRACE','sentenciaSwitch',5,'p_switchNoCondicion','parserGo.py',39),
  ('bloqueCasosBooleanos -> casoBooleano','bloqueCasosBooleanos',1,'p_bloqueCasosBooleanos','parserGo.py',42),
  ('bloqueCasosBooleanos -> casoBooleano bloqueCasosBooleanos','bloqueCasosBooleanos',2,'p_bloqueCasosBooleanos','parserGo.py',43),
  ('casoBooleano -> CASE condiciones DOSPUNTOS subcodigo','casoBooleano',4,'p_casoBooleano','parserGo.py',46),
  ('casoBooleano -> CASE ID DOSPUNTOS subcodigo','casoBooleano',4,'p_casoBooleano','parserGo.py',47),
  ('casoDefault -> DEFAULT DOSPUNTOS subcodigo','casoDefault',3,'p_casoDefault','parserGo.py',50),
  ('casoDefault -> empty','casoDefault',1,'p_casoDefault','parserGo.py',51),
  ('bloqueCasosSwitch -> casoSwitch','bloqueCasosSwitch',1,'p_bloqueCasosSwitch','parserGo.py',54),
  ('bloqueCasosSwitch -> casoSwitch bloqueCasosSwitch','bloqueCasosSwitch',2,'p_bloqueCasosSwitch','parserGo.py',55),
  ('casoSwitch -> CASE valores DOSPUNTOS subcodigo','casoSwitch',4,'p_casoSwitch','parserGo.py',58),
  ('estructurasDeDatos -> mapa','estructurasDeDatos',1,'p_estructurasDeDatos','parserGo.py',63),
  ('mapa -> MAP LBRACKET tipoDato RBRACKET tipoDato LBRACE RBRACE','mapa',7,'p_definicionMapaVacio','parserGo.py',66),
  ('mapa -> MAP LBRACKET tipoDato RBRACKET tipoDato LBRACE elementosMapa RBRACE','mapa',8,'p_definicionMapaValores','parserGo.py',69),
  ('elementosMapa -> elementoMapa','elementosMapa',1,'p_elementosMapa','parserGo.py',72),
  ('elementosMapa -> elementoMapa elementosMapa','elementosMapa',2,'p_elementosMapa','parserGo.py',73),
  ('elementoMapa -> valor DOSPUNTOS valor COMMA','elementoMapa',4,'p_elementoMapa','parserGo.py',76),
  ('asignacion -> VAR ID tipoDato EQUAL valor','asignacion',5,'p_asignacionTipo','parserGo.py',80),
  ('asignacion -> VAR ID EQUAL valor','asignacion',4,'p_asignacionInferencia','parserGo.py',83),
  ('asignacionCorta -> ID DOSPUNTOS EQUAL valor','asignacionCorta',4,'p_asignacionCorta','parserGo.py',86),
  ('tipoDato -> FLOAT64_TYPE','tipoDato',1,'p_tipoDato','parserGo.py',89),
  ('tipoDato -> COMPLEX64_TYPE','tipoDato',1,'p_tipoDato','parserGo.py',90),
  ('tipoDato -> INT_TYPE','tipoDato',1,'p_tipoDato','parserGo.py',91),
  ('tipoDato -> BOOL_TYPE','tipoDato',1,'p_tipoDato','parserGo.py',92),
  ('tipoDato -> STRING_TYPE','tipoDato',1,'p_tipoDato','parserGo.py',93),
  ('valores -> valor','valores',1,'p_valores','parserGo.py',96),
  ('valores -> valor COMMA valores','valores',3,'p_valores','parserGo.py',97),
  ('valor -> FLOAT64','valor',1,'p_valor','parserGo.py',100),
  ('valor -> COMPLEX64','valor',1,'p_valor','parserGo.py',101),
  ('valor -> INT','valor',1,'p_valor','parserGo.py',102),
  ('valor -> BOOL','valor',1,'p_valor','parserGo.py',103),
  ('valor -> STRING','valor',1,'p_valor','parserGo.py',104),
  ('valor -> expresionesAritmeticas','valor',1,'p_valor','parserGo.py',105),
  ('valor -> condiciones','valor',1,'p_valor','parserGo.py',106),
  ('valor -> ID','valor',1,'p_valor','parserGo.py',107),
  ('valor -> estructurasDeDatos','valor',1,'p_valor','parserGo.py',108),
  ('expresionesAritmeticas -> expresionAritmetica','expresionesAritmeticas',1,'p_expresionesAritmeticas','parserGo.py',112),
  ('expresionesAritmeticas -> expresionAritmetica operador expresionesAritmeticas','expresionesAritmeticas',3,'p_expresionesAritmeticas','parserGo.py',113),
  ('expresionAritmetica -> valor operador valor','expresionAritmetica',3,'p_expresionAritmetica','parserGo.py',116),
  ('expresionAritmetica -> LPAREN valor operador valor RPAREN','expresionAritmetica',5,'p_expresionAritmetica','parserGo.py',117),
  ('operador -> PLUS','operador',1,'p_operador','parserGo.py',120),
  ('operador -> MINUS','operador',1,'p_operador','parserGo.py',121),
  ('operador -> TIMES','operador',1,'p_operador','parserGo.py',122),
  ('operador -> DIVIDE','operador',1,'p_operador','parserGo.py',123),
  ('operador -> MOD','operador',1,'p_operador','parserGo.py',124),
  ('condiciones -> condicion','condiciones',1,'p_condiciones','parserGo.py',128),
  ('condiciones -> condicion conector condiciones','condiciones',3,'p_condiciones','parserGo.py',129),
  ('conector -> AND','conector',1,'p_conector','parserGo.py',132),
  ('conector -> OR','conector',1,'p_conector','parserGo.py',133),
  ('condicion -> valor operadorComp valor','condicion',3,'p_condicion','parserGo.py',136),
  ('condicion -> BOOL','condicion',1,'p_condicion','parserGo.py',137),
  ('operadorComp -> NOT_EQUAL','operadorComp',1,'p_operadorComparacion','parserGo.py',140),
  ('operadorComp -> LESS_THAN','operadorComp',1,'p_operadorComparacion','parserGo.py',141),
  ('operadorComp -> LESS_EQUAL','operadorComp',1,'p_operadorComparacion','parserGo.py',142),
  ('operadorComp -> GREATER_THAN','operadorComp',1,'p_operadorComparacion','parserGo.py',143),
  ('operadorComp -> GREATER_EQUAL','operadorComp',1,'p_operadorComparacion','parserGo.py',144),
  ('empty -> <empty>','empty',0,'p_empty','parserGo.py',147),
  ('imprimir -> FMT PUNTO PRINT_LN LPAREN valores RPAREN','imprimir',6,'p_imprimir','parserGo.py',152),
  ('imprimir -> FMT PUNTO PRINT_LN LPAREN RPAREN','imprimir',5,'p_imprimir','parserGo.py',153),
]
