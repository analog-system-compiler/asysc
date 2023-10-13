/*******************************************************************************/
/*  Copyright (C) 2023 The LightCAS project                                     */
/*                                                                             */
/*  This program is free software; you can redistribute it and/or modify       */
/*  it under the terms of the GNU General Public License as published by       */
/*  the Free Software Foundation; either version 2 of the License, or          */
/*  (at your option) any later version.                                        */
/*                                                                             */
/*  This program is distributed in the hope that it will be useful,            */
/*  but WITHOUT ANY WARRANTY; without even the implied warranty of             */
/*  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the              */
/*  GNU General Public License for more details.                               */
/*                                                                             */
/*  You should have received a copy of the GNU General Public License          */
/*  along with this program; if not, write to the Free Software                */
/*  Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA. */
/*******************************************************************************/

#include <cstdio>
#include <iostream>
#include <string>
#include "Parser.h"
#include "Display.h"
#include "CMathExpressionEx.h"

int main(int argc, char *argv[])
{
  setlocale(LC_NUMERIC, "C");
  std::cout << "*************************************\n";
  std::cout << "*** LighCAS Console               ***\n";
  std::cout << "*** (C)  Cyril Collineau 2023     ***\n";
  std::cout << "*************************************\n";
  std::cout << "Type \"help\" for help.\n";

  CEvaluator eval;
  CElementDataBase db_root("Root", NULL, &eval);
  CElementDataBase db("User", &db_root);
  // CElement *simplify = db.GetElement("SIMPLIFY");
  // CElement *ans = db.GetElement("ans");
  // OP_CODE simplify_op = simplify->ToRef();
  CMathExpressionEx equ(&db);
  CDisplay ds;
  CParser parser;

  if (argc == 1)
  {
    parser.LoadFile(argv[1]);    
    equ.ToPython(parser,ds);
  }

  return 0;
}

