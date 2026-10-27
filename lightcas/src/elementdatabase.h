/*
 * Copyright (C) 2006-2025 The LightCAS project
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3 of the License, or
 * any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; If not, see <https://www.gnu.org/licenses/>
 */

#pragma once

#include "lcstring.h"
#include "parser.h"
#include "evaluator.h"
#include "lcvector.h"

class CMathExpression;
class CElement;
struct CSymbolSyntaxStruct;

typedef CVector<CElement *> CElementArray;
typedef CVector<struct CSymbolSyntaxStruct *> CSymbolSyntaxArray;

constexpr OP_CODE PackCode(unsigned op, unsigned operand_nb)
{
  return static_cast<OP_CODE>((op & CODE_MASK) | ((operand_nb & 0x3u) << 14));
}

struct SProperties
{
  const char *m_FunctionName;
  unsigned m_ParameterNb;
  CEvaluatorFunct m_FunctionCall;
};

class CElementDataBase : public CElementArray
{

protected:
  CString m_Name;
  CString m_RootPath;
  CElementDataBase *m_Parent;
  CEvaluator *m_Evaluator;
  unsigned m_SearchStart;
  bool m_Error;
  unsigned char m_Precedence;
  static unsigned m_SecureLimit;
  static CElementArray m_ElementRefArray;
  static CSymbolSyntaxArray m_SymbolSyntaxArray;
  static const SProperties m_FunctionProperties[];
  static const unsigned m_FunctionPropertiesSize;

public:
  static constexpr OP_CODE Pack(unsigned op, unsigned operand_nb)
  {
    return PackCode(op, operand_nb);
  }

  static constexpr unsigned GetOperandNb(OP_CODE op) { return static_cast<unsigned>((op >> 14) & 0x3u); }
  static constexpr unsigned GetOperator(OP_CODE op) { return static_cast<unsigned>(op & CODE_MASK); }
  static constexpr OP_CODE OP_PAR0 = PackCode(0, 0);
  static constexpr OP_CODE OP_PAR1 = PackCode(1, 0);
  static constexpr OP_CODE OP_PAR2 = PackCode(2, 0);
  static constexpr OP_CODE OP_PAR3 = PackCode(3, 0);
  static constexpr OP_CODE OP_PAR4 = PackCode(4, 0);
  static constexpr OP_CODE OP_PAR5 = PackCode(5, 0);
  static constexpr OP_CODE OP_PAR6 = PackCode(6, 0);
  static constexpr OP_CODE OP_PAR7 = PackCode(7, 0);
  static constexpr OP_CODE OP_PAR8 = PackCode(8, 0);
  static constexpr OP_CODE OP_PAR9 = PackCode(9, 0);
  static constexpr OP_CODE OP_PARA = PackCode(10, 0);
  static constexpr OP_CODE OP_PARB = PackCode(11, 0);
  static constexpr OP_CODE OP_PARC = PackCode(12, 0);
  static constexpr OP_CODE OP_PARD = PackCode(13, 0);
  static constexpr OP_CODE OP_PARE = PackCode(14, 0);
  static constexpr OP_CODE OP_PARF = PackCode(15, 0);
  static constexpr OP_CODE OP_ZERO = PackCode(16, 0);
  static constexpr OP_CODE OP_SET = PackCode(17, 2);
  static constexpr OP_CODE OP_GET = PackCode(18, 1);
  static constexpr OP_CODE OP_NONE = PackCode(19, 0);
  static constexpr OP_CODE OP_CONST = PackCode(20, 1);
  static constexpr OP_CODE OP_ELEM = PackCode(21, 1);
  static constexpr OP_CODE OP_FUNCT0 = PackCode(22, 1);
  static constexpr OP_CODE OP_FUNCT1 = PackCode(23, 2);
  static constexpr OP_CODE OP_FUNCT2 = PackCode(24, 3);
  static constexpr OP_CODE OP_NEG = PackCode(25, 1);
  static constexpr OP_CODE OP_EVAL = PackCode(26, 1);
  static constexpr OP_CODE OP_CHECK = PackCode(27, 2);
  static constexpr OP_CODE OP_PRINT = PackCode(28, 1);
  static constexpr OP_CODE OP_EXEC = PackCode(29, 1);

  static constexpr unsigned MAX_EXP = 30;
  static constexpr unsigned MAX_PAR = 16;

protected:
  unsigned Register(CElement *e, unsigned index);
  CElement *CreateElement(const CString &string, unsigned pos);
  virtual void AddReservedElements();
  virtual void AddReservedFunctions();
  virtual void AddEvalFunctionTable(const SProperties *property_table, unsigned size);
  virtual void AddEvalFunction(const CString &name, unsigned parameter_nb, CEvaluatorFunct funct);
  void InitAlgebraRuleTable();
  void CleanTempElements();
  static void SetSecureLimit(unsigned i) { m_SecureLimit = i; }

public:
  void Clear();
  bool IsOK() { return !m_Error; }
  const CString &GetName() const { return m_Name; }
  const CString &GetRootPath() const { return m_RootPath; }
  void SetName(const CString &name) { m_Name = name; }
  bool Initialize();
  CEvaluator *GetEvaluator() const { return m_Evaluator; }
  void SetEvaluator(CEvaluator *eval) { m_Evaluator = eval; }
  CElement *ParseElement(CParser &IC);
  CElement *GetElement();
  CElement *GetElement(const CString &);
  CElement *SearchElement(const CString &, unsigned &pos) const;
  bool AssociateSymbol(CParser &IC);
  bool LoadFromFile(const CString &file_name, CMathExpression &src);

  // static OP_CODE    ElementToRef( const CElement* e );
  static CElement *RefToElement(OP_CODE op) { return m_ElementRefArray[GetOperator(op)]; }
  static void UnRef(OP_CODE op) { m_ElementRefArray[GetOperator(op)] = NULL; }
  static const CSymbolSyntaxArray &GetSymbolTable() { return m_SymbolSyntaxArray; }
  // static unsigned GetSecureLimit() { return m_SecureLimit; }
  static bool IsReservedElement(OP_CODE op) { return (GetOperator(op) < m_SecureLimit); }
  static bool IsParameterOP(OP_CODE op) { return (GetOperator(op) >= GetOperator(OP_PAR0)) && (GetOperator(op) <= GetOperator(OP_PARF)); }
  static bool IsFunctionOP(OP_CODE op) { return (GetOperator(op) >= GetOperator(OP_CONST)) && (GetOperator(op) <= GetOperator(OP_FUNCT2)); }
  CElementDataBase *GetParent() const { return m_Parent; }

#ifdef _TEST
  void Test();
  void Check(const char *s1, const char *s2);
  void CheckEval(const char *s1, const CValue &v1);
  void CheckSyntaxError(const char *s1);
  void DisplayStats();
#endif

  explicit CElementDataBase(const CElementDataBase &db); // avoid simple copy
  explicit CElementDataBase(const CString &name = CString(), CElementDataBase *db = NULL, CEvaluator *eval = NULL, const CString &exe_path = CString());
  virtual ~CElementDataBase();
};
