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
#include <unistd.h>
#include "Parser.h"
#include "Display.h"
#include "CMathExpressionEx.h"

// #define _TEST

int main(int argc, char *argv[])
{
  char *input_filename = NULL;
  char *output_filename = NULL;
  CAnalysisMode analysis_type;

  while (true)
  {
    switch (getopt(argc, argv, "i:o:t:"))
    {
    case 'i':
      input_filename = optarg;
      continue;
    case 'o':
      output_filename = optarg;
      continue;
    case 't':
      if (!strcmp(optarg, "ac"))
        analysis_type = CAnalysisMode::AC_ANALYSIS;
      else if (!strcmp(optarg, "trans"))
        analysis_type = CAnalysisMode::TRANS_ANALYSIS;
      continue;
    case '?':
      if (optopt == 'i' or optopt == 'o')
        fprintf(stderr, "Option -%c requires an argument.\n", optopt);
      else if (isprint(optopt))
        fprintf(stderr, "Unknown option `-%c'.\n", optopt);
      else
        fprintf(stderr, "Unknown option character `\\x%x'.\n", optopt);
      return 1;
    case -1:
      break;
    default:
      abort();
    }
    break;
  }

  CEvaluator eval;
  CElementDataBase db_root("Root", NULL, &eval, true, argv[0]);
  CElementDataBase db("User", &db_root);
  CMathExpressionEx equ(&db);
  CDisplay ds;
  CParser parser;

#ifdef _TEST
  db.Test();
  db.Initialize();
#endif

  if (!db.IsOK())
    return 1;

  if (parser.LoadFromFile(CParser::GetPath(argv[0]) + input_filename))
    if (ds.StoreToFile(output_filename))
      equ.ToPython(parser, ds, analysis_type);

  return 0;
}
